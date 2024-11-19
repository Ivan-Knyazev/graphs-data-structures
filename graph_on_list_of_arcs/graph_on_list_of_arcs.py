from typing import List, Union


class Arc:
    def __init__(self, from_vertex: str, to_vertex: str, weight: int):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __repr__(self):
        return f"Arc({self.from_vertex} -> {self.to_vertex}, weight={self.weight})"


class Graph:
    """Граф на списке дуг"""

    def __init__(self):
        self.arcs = []         # Список дуг
        self.vertices = set()  # Множество вершин

    # Добавление ребра в граф (если его ещё нет)
    def add_arc(self, from_vertex: str, to_vertex: str, weight: int) -> None:
        for arc in self.arcs:
            if arc.from_vertex == from_vertex and arc.to_vertex == to_vertex:
                return
        new_arc = Arc(from_vertex, to_vertex, weight)
        self.arcs += [new_arc]
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

    # Удаление рёбра из графа
    def remove_arc(self, from_vertex, to_vertex) -> None:
        self.arcs = [arc for arc in self.arcs if not (
            arc.from_vertex == from_vertex and arc.to_vertex == to_vertex)]
        self.vertices.clear()
        for arc in self.arcs:
            self.vertices.add(arc.from_vertex)
            self.vertices.add(arc.to_vertex)

    # Поиск рёбер по начальной и конечной вершинам
    def find_arc(self, from_vertex: str, to_vertex: str) -> Union[Arc, None]:
        for arc in self.arcs:
            if arc.from_vertex == from_vertex and arc.to_vertex == to_vertex:
                return arc
        return None

    # Добавление вершины (если её ещё нет)
    def add_vertex(self, vertex: str) -> None:
        self.vertices.add(vertex)

    # Удаление вершины (и соответствующих рёбер)
    def remove_vertex(self, vertex: str) -> None:
        self.vertices.discard(vertex)
        self.arcs = [arc for arc in self.arcs if not (
            arc.from_vertex == vertex or arc.to_vertex == vertex)]

    # Поиск вершины
    def find_vertex(self, vertex: str) -> bool:
        return vertex in self.vertices

    # Получение сортированного списка вершин графа
    def get_vertices(self) -> List[str]:
        return list(sorted(self.vertices))

    # Форматированный вывод графа
    def __repr__(self):
        output = "Graph:\n"
        vertices_in_arcs = set()
        for arc in self.arcs:
            vertices_in_arcs.add(arc.from_vertex)
            vertices_in_arcs.add(arc.to_vertex)
            output += f"  {arc.from_vertex} -> " + \
                f"{arc.to_vertex} (weight={arc.weight})" + "\n"
        # sorted(self.vertices) self.vertices.difference(vertices_in_arcs)
        for vertex in self.vertices.difference(vertices_in_arcs):
            output += f"  {vertex}" + "\n"
        return output.strip()
