from custom_structure.Graph import Graph
from image_output import save, save_graph
from logic import input_parse


def different_in_list(list1, list2):
    list = []
    for elem in list1:
        if elem not in list2:
            list.append(elem)
    for elem in list2:
        if elem not in list1:
            list.append(elem)
    return list


def delete_update(value, first_tree_pairs, second_tree_pairs):
    differ = different_in_list(first_tree_pairs, second_tree_pairs)
    print("Different: ", differ)

    first_tree_pairs = new_edges(first_tree_pairs, value)
    print("First tree pairs: ", first_tree_pairs)
    second_tree_pairs = new_edges(second_tree_pairs, value)
    print("Second tree pairs: ", second_tree_pairs)

    graph_edges = first_tree_pairs.copy()
    for pair in second_tree_pairs:
        if pair not in graph_edges:
            graph_edges.append(pair)
    graph = Graph(1).create_from_list(graph_edges)

    # sorted(graph_edges, key=lambda x: x[0])
    # graph = Graph(1).create_from_list(graph_edges)
    return graph, graph_edges, first_tree_pairs, second_tree_pairs


def new_edges(graph_edges, value):
    end_with_value = []
    start_with_value = []
    edge_copy = graph_edges.copy()
    for edge in graph_edges:
        if edge[0] == value:
            start_with_value.append(edge[1])
            edge_copy.remove(edge)
        if edge[1] == value:
            end_with_value.append(edge[0])
            edge_copy.remove(edge)
    for start in start_with_value:
        for end in end_with_value:
            if (end, start) not in edge_copy:
                edge_copy.append((end, start))
    return edge_copy


def find_all_cycles(graph):
    cycles = []

    def find_cycle(node, path):
        if node.value in path:
            if len(path[path.index(node.value):]) > 2:
                cycles.append(path[path.index(node.value):])
            return
        path.append(node.value)
        for neighbor in node.neighbors:
            find_cycle(neighbor, path.copy())
        return

    find_cycle(graph, [])
    cycles = cycles_unique(cycles)
    return cycles


def cycles_unique(cycles):
    new_cycles = []
    for cycle in cycles:
        flag = True
        for i in range(len(cycle)):
            temp_cycle = cycle[i:] + cycle[:i]
            if temp_cycle in new_cycles:
                flag = False
                break
            if temp_cycle[::-1] in new_cycles:
                flag = False
                break
        if flag:
            new_cycles.append(cycle)
    return new_cycles


def count_transitive_edges(nodes_values, edges):
    minimum = []
    minimum_val = 2 ** 32
    answer = {}
    for node_val in nodes_values:
        end_with_value = []
        start_with_value = []

        for edge in edges:
            if edge[0] == node_val:
                start_with_value.append(edge[1])
            if edge[1] == node_val:
                end_with_value.append(edge[0])

        count = len(end_with_value) * len(start_with_value)

        for start in start_with_value:
            for end in end_with_value:
                if (end, start) in edges:
                    count -= 1
                if (start, end) in edges:
                    count -= 1
        answer[node_val] = count

        if count == minimum_val:
            minimum.append(node_val)
        if count < minimum_val:
            minimum_val = count
            minimum = [node_val]
    return answer, minimum


def count_val_in_cycles(cycles):
    output = {}
    for cycle in cycles:
        for val in cycle:
            if val == 1:
                continue
            if val in output:
                output[val] += 1
            else:
                output[val] = 1
    return output


def graph_main(m_nodes=0, first_tree_pairs=None, second_tree_pairs=None):
    #m_nodes, first_tree_pairs, second_tree_pairs = input_parse()

    first_tree_pairs = [(1, 2), (1, 4), (1, 7), (2, 12), (2, 3),
                        (3, 10), (4, 11), (4, 5), (4, 14),
                        (5, 9), (5, 15), (7, 8), (7, 6),
                        (8, 13)]
    second_tree_pairs = [(1, 6), (1, 2), (1, 13), (1, 7),
                         (6, 3), (3, 4), (3, 5),
                         (2, 11), (2, 8), (13, 12),
                         (13, 15), (13, 10),
                         (7, 14), (14, 9)]
    m_nodes = 15

    print("First tree pairs: ", first_tree_pairs)
    print("Second tree pairs: ", second_tree_pairs)

    differ = different_in_list(first_tree_pairs, second_tree_pairs)
    print("Different: ", differ)

    graph_edges = first_tree_pairs.copy()
    for pair in second_tree_pairs:
        if pair not in graph_edges:
            graph_edges.append(pair)
    graph = Graph(1).create_from_list(graph_edges)

    cycles = find_all_cycles(graph)
    deleted = []

    photo_counter = 0
    save_graph(root=graph, filename=f'img/graph_{photo_counter}')
    photo_counter += 1

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

        save_graph(root=graph, filename=f'img/graph_{photo_counter}')
        photo_counter += 1

        print("_______________________________________")
        print("Graph edges: ", graph_edges)
        differ = different_in_list(first_tree_pairs, second_tree_pairs)
        cycles = find_all_cycles(graph)

    differ = different_in_list(first_tree_pairs, second_tree_pairs)
    print("Different: ", differ)

    print("Answer: ", len(deleted))
    print("Deleted: ", deleted)

    save_graph(root=graph, filename=f'img/graph_{photo_counter}')
    photo_counter += 1

    return len(deleted)


if __name__ == "__main__":
    graph_main()
