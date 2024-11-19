from typing import Dict, List


class Graph:
    """Граф на списке смежности"""

    def __init__(self) -> None:
        self.adjacency_list: Dict[str, Dict[str, int]] = {}  # Список смежности

    # Добавление ребра в граф (если его ещё нет)
    def add_edge(self, from_vertex: str, to_vertex: str, weight: int) -> None:
        if from_vertex not in self.adjacency_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.add_vertex(to_vertex)

        self.adjacency_list[from_vertex][to_vertex] = weight

    # Удаление рёбра из графа
    def remove_edge(self, from_vertex, to_vertex) -> None:
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].pop(to_vertex, None)

    # Поиск рёбер по начальной и конечной вершинам
    def has_edge(self, from_vertex: str, to_vertex: str) -> bool:
        return from_vertex in self.adjacency_list and to_vertex in self.adjacency_list[from_vertex]

    # Добавление вершины (если её ещё нет)
    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = dict()

    # Удаление вершины (и соответствующих рёбер)
    def remove_vertex(self, vertex: str) -> None:
        if vertex in self.adjacency_list:
            self.adjacency_list.pop(vertex, None)

            for vert in self.adjacency_list:
                if vertex in self.adjacency_list[vert]:
                    self.adjacency_list[vert].pop(vertex, None)

    # Поиск вершины
    def has_vertex(self, vertex: str) -> bool:
        return vertex in self.adjacency_list

    # Получение сортированного списка вершин графа
    def get_vertices(self) -> List[str]:
        return list(sorted(self.adjacency_list.keys()))

    # Форматированный вывод графа
    def __repr__(self):
        v_output = set()
        v_none_output = set()
        output = "Graph:\n"
        for from_vertex, edges in self.adjacency_list.items():
            if len(edges) == 0:
                v_none_output.add(from_vertex)
            for to_vertex, weight in edges.items():
                output += f"{from_vertex} -> {to_vertex} (weight: {weight}) \n"
                v_output.add(from_vertex)
                v_output.add(to_vertex)
        output += "\n".join(f"{v}" for v in v_none_output.difference(v_output))
        return output.strip()
