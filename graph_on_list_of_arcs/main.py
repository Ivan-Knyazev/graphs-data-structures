from graph_on_list_of_arcs import Graph


# Функция для визуального тестирования написанного графа
def test_graph():
    # Пример использования
    graph = Graph()

    # Работа с рёбрами:
    # Добавление рёбер
    graph.add_arc('A', 'B', 5)
    graph.add_arc('A', 'C', 10)
    graph.add_arc('B', 'C', 2)
    graph.add_arc('B', 'D', 12)
    print("Start Graph -", graph)

    # Поиск ребра
    arc = graph.find_arc('A', 'B')
    print("Find arc AB:", arc)

    # Удаление ребра
    graph.remove_arc('A', 'B')
    print("Graph after remove arc AB -", graph)
    print('-'*100)

    # Работа с вершинами:
    # Добавление вершин
    graph.add_vertex('K')
    graph.add_vertex('U')
    graph.add_vertex('F')
    print("New Graph after add new vertices -", graph)

    # Проверка вершины на наличие в графе
    vertex_A, vertex_T = 'A', 'T'
    status_A = graph.find_vertex(vertex_A)
    status_T = graph.find_vertex(vertex_T)
    print(f"Vertex {vertex_A} status:", status_A)
    print(f"Vertex {vertex_T} status:", status_T)

    # Получение всех вершин
    vertices = graph.get_vertices()
    print("Vertices:", vertices)

    # Удаление вершины
    graph.remove_vertex('A')
    print("Graph after remove vertex A -", graph)
    print('-'*100)

    # Дополнительные проверки:
    # Добавление рёбер на те вершины, которые были одиночными
    graph.add_arc('F', 'K', 5)
    graph.add_arc('C', 'F', 10)
    print("New Graph after add new arcs -", graph)


if __name__ == "__main__":
    print("[INFO] Starting testing app")
    test_graph()
