from typing import List, Union


class Edge:
    def __init__(self, from_vertex: str, to_vertex: str, weight: int):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __repr__(self):
        return f"Edge({self.from_vertex} -> {self.to_vertex}, weight={self.weight})"


class Graph:
    """Граф на списке рёбер"""

    def __init__(self):
        self.edges = []        # Список рёбер
        self.vertices = set()  # Множество вершин

    # Добавление ребра в граф (если его ещё нет)
    def add_edge(self, from_vertex: str, to_vertex: str, weight: int) -> None:
        for edge in self.edges:
            if edge.from_vertex == from_vertex and edge.to_vertex == to_vertex:
                return
        new_edge_forward = Edge(from_vertex, to_vertex, weight)
        new_edge_backward = Edge(to_vertex, from_vertex, weight)
        self.edges += [new_edge_forward, new_edge_backward]
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

    # Удаление рёбра из графа
    def remove_edge(self, from_vertex, to_vertex) -> None:
        self.edges = [edge for edge in self.edges if not (
            (edge.from_vertex == from_vertex and edge.to_vertex == to_vertex) or
            (edge.from_vertex == to_vertex and edge.to_vertex == from_vertex))]
        self.vertices.clear()
        for edge in self.edges:
            self.vertices.add(edge.from_vertex)
            self.vertices.add(edge.to_vertex)

    # Поиск рёбер по начальной и конечной вершинам
    def find_edge(self, from_vertex: str, to_vertex: str) -> Union[Edge, None]:
        for edge in self.edges:
            if edge.from_vertex == from_vertex and edge.to_vertex == to_vertex:
                return edge
        return None

    # Добавление вершины (если её ещё нет)
    def add_vertex(self, vertex: str) -> None:
        self.vertices.add(vertex)

    # Удаление вершины (и соответствующих рёбер)
    def remove_vertex(self, vertex: str) -> None:
        self.vertices.discard(vertex)
        self.edges = [edge for edge in self.edges if not (
            edge.from_vertex == vertex or edge.to_vertex == vertex)]

    # Поиск вершины
    def find_vertex(self, vertex: str) -> bool:
        return vertex in self.vertices

    # Получение сортированного списка вершин графа
    def get_vertices(self) -> List[str]:
        return list(sorted(self.vertices))

    # Форматированный вывод графа
    def __repr__(self):
        output = "Graph:\n"
        vertices_in_edges = set()
        for edge in self.edges:
            vertices_in_edges.add(edge.from_vertex)
            vertices_in_edges.add(edge.to_vertex)
            output += f"  {edge.from_vertex} -> " + \
                f"{edge.to_vertex} (weight={edge.weight})" + "\n"
        # sorted(self.vertices) self.vertices.difference(vertices_in_edges)
        for vertex in self.vertices.difference(vertices_in_edges):
            output += f"  {vertex}" + "\n"
        return output.strip()
