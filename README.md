# TestTask

## Задание
Сбалансировать путём удаления вершин

## Решение
1. main.py - первое из решений, голосование узлов
2. not_green.py - второе из решений, полный перебор
3. graph_main.py - бонусное решение с использованием графов

## Структуры данных
1. TreeNode - узел дерева
2. Graph - узел графа

# main.py

1. Считывание данных
```python 
from logic import input_parse
m_nodes, first_tree_pairs, second_tree_pairs = input_parse()
```
2. Создание деревьев
```python
from custom_structures import TreeNode
first_tree = TreeNode(1).create_from_list(first_tree_pairs)
second_tree = TreeNode(1).create_from_list(second_tree_pairs)
```

3. Поиск "худших" узлов - те, что стоят не на своём месте
и дальнейшая обработка, сложность приблизительно O(n^2)
```python
    while worst_parent:
        worst_parent = find_worst_parent(m_nodes, first_tree, second_tree)
        deleted.append(worst_parent)

        first_tree.delete(worst_parent)
        second_tree.delete(worst_parent)

    answer = len(deleted) - 1
    print("Answer: ", answer)
    print("Deleted: ", deleted)
```

4. Визуализация - сохранением графа в файл
```python
first_tree.save(filename=f'img/first/tree_{photo_counter}')
second_tree.save(filename=f'img/second/tree_{photo_counter}')
photo_counter += 1
```

5. Визуализация - создание видео
```python
from image_output import video_create
video_create(path="img/first")
video_create(path="img/second")
```

# not_greedy_main.py
1. Считывание данных
```python 
from logic import input_parse
m_nodes, first_tree_pairs, second_tree_pairs = input_parse()
```
2. Создание деревьев
```python
first_tree = TreeNode(1).create_from_list(first_tree_pairs)
second_tree = TreeNode(1).create_from_list(second_tree_pairs)
```
3. Полный перебор и немного оптимизации памяти генератором и маской
```python
def node_list_generator(m_nodes):
    bit_mask = 0
    list = [i for i in range(2, m_nodes + 1)]
    while bit_mask != (2 ** (m_nodes - 1)) - 1:
        yield [list[i] for i in range(m_nodes) if bit_mask & (1 << i)]
        bit_mask += 1

for i in range(1, 2 **(m_nodes - 1)):
        new_list = next(list_gen)
        if len(new_list) > min_len:
            continue
        first_tree.delete_list(new_list)
        second_tree.delete_list(new_list)
        if first_tree == second_tree and len(new_list) <= min_len:
            print("Found: ", new_list)
            answer_list.append(new_list)
            min_len = len(new_list)
        first_tree = TreeNode(1).create_from_list(first_tree_pairs)
        second_tree = TreeNode(1).create_from_list(second_tree_pairs)
```

# graph_main.py
1. Считывание данных
```python 
from logic import input_parse
m_nodes, first_tree_pairs, second_tree_pairs = input_parse()
```
2. Создание деревьев
```python
graph_edges = first_tree_pairs.copy()
    for pair in second_tree_pairs:
        if pair not in graph_edges:
            graph_edges.append(pair)
    graph = Graph(1).create_from_list(graph_edges)

    cycles = find_all_cycles(graph)
```
2. Логика - сделать из 2х деревьев граф, с заранее известными 
правилами удаления
и избавиться от циклов в графе
```python
    while cycles or differ:

        if not cycles:
            differ = different_in_list(first_tree_pairs, second_tree_pairs)
            differ_map = {}
            for pair in differ:
                for val in pair:
                    if val == 1:
                        continue
                    if val in differ_map:
                        differ_map[val] += 1
                    else:
                        differ_map[val] = 1
            max_elements = [key for key, value in differ_map.items() if value == max(differ_map.values())]
            print("Max elements: ", max_elements)
            print("Differ: ", differ_map)

            max_el = max_elements[0]
            graph, graph_edges, first_tree_pairs, second_tree_pairs = delete_update(max_el, first_tree_pairs,
                                                                                    second_tree_pairs)
            deleted.append(max_el)
            differ = different_in_list(first_tree_pairs, second_tree_pairs)
            cycles = find_all_cycles(graph)
            continue

        val_in_cycles = count_val_in_cycles(cycles)
        max_elements = [key for key, value in val_in_cycles.items() if value == max(val_in_cycles.values())]
        print("Max elements: ", max_elements)

        all_possible, mins = count_transitive_edges(max_elements, graph_edges)
        print("All possible: ", all_possible)
        print("Mins: ", mins)

        worst_elem = mins[0]
        graph, graph_edges, first_tree_pairs, second_tree_pairs = delete_update(worst_elem, first_tree_pairs,
                                                                                second_tree_pairs)
        deleted.append(worst_elem)
        print("Deleted: ", deleted)

        graph.save_graph(filename=f'img/graph/graph_{photo_counter}')
        photo_counter += 1

        print("_______________________________________")
        print("Graph edges: ", graph_edges)
        differ = different_in_list(first_tree_pairs, second_tree_pairs)
        cycles = find_all_cycles(graph)
```

4. Визуализация - сохранением графа в файл
```python
graph.save_graph(filename=f'img/graph/graph_{photo_counter}')
photo_counter += 1
```