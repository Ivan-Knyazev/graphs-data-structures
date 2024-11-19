# Набор классов Graph, реализующий представление ориентированного взвешенного графа в виде различных структур данных


## Инструкция
Каждый тип графа распологается в соответствующей папке. Реализация находится в файлах с названиями, аналогичными названиям директорий. Клиентский код для проверки работоспособности написанных классов - в файлах `main.py`, консольный вывод данных тестовых программ - в файлах `output.txt`.

## Структура проекта
```bash
.
├── graph_on_adjacency_list
│   ├── graph_on_adjacency_list.py
│   ├── main.py
│   └── output.txt
├── graph_on_arc_bundles
│   ├── graph_on_arc_bundles.py
│   ├── main.py
│   └── output.txt
├── graph_on_list_of_arcs
│   ├── graph_on_list_of_arcs.py
│   ├── main.py
│   └── output.txt
├── graph_on_list_of_edges
│   ├── graph_on_list_of_edges.py
│   ├── main.py
│   └── output.txt
└── README.md

5 directories, 13 files
```

## О работе
В данном репозитории представлены различные реализации графов по следующей задаче:

    Разработать набор классов Graph, реализующий представление ориентированного взвешенного графа в виде следующих структур данных: список ребер, список дуг, список смежности, список пучков дуг. Также необходимо поддерживать операции удаления, вставки и поиска вершин/ребер.

<hr>

Выполнено в рамках дисциплины "Комбинаторика и теория графов" на 2 курсе в НИТУ МИСИС, 19.11.24
