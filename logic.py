from custom_structure.Graph import Graph


def input_parse():
    max_nodes = int(input())
    first_tree_pairs = []
    second_tree_pairs = []

    _ = input()

    line = input()
    while line != "Tree2":
        first_tree_pairs.append(tuple(map(int, line.split())))
        line = input()

    line = input()
    while line != "":
        second_tree_pairs.append(tuple(map(int, line.split())))
        line = input()

    return max_nodes, first_tree_pairs, second_tree_pairs


def find_worst_parent(m_nodes, first_tree, second_tree):
    bad_parents = [0] * (m_nodes + 1)

    for i in range(2, m_nodes):
        first_tree_el = first_tree.search(i)
        second_tree_el = second_tree.search(i)

        if first_tree_el is None or second_tree_el is None:
            continue
        if first_tree_el.parent.value != second_tree_el.parent.value:
            bad_parents[first_tree_el.parent.value] += 1
            bad_parents[second_tree_el.parent.value] += 1

    print(bad_parents[1:])

    worst_parent = 0

    for i in range(1, m_nodes + 1):
        if bad_parents[i] > bad_parents[worst_parent]:
            worst_parent = i

    if worst_parent == 1:
        worst_parent = 0
        trees_values = set([el.value for el in first_tree.children + second_tree.children])
        for el in trees_values:
            if bad_parents[el] > bad_parents[worst_parent]:
                worst_parent = el
        print(worst_parent)
        return worst_parent

    if worst_parent == 0:
        return False

    print(worst_parent)
    return worst_parent

def find_bad_nodes(m_nodes, first_tree, second_tree):

    bad_nodes = set()

    for i in range(2, m_nodes + 1):
        first_tree_el = first_tree.search(i)
        second_tree_el = second_tree.search(i)

        if first_tree_el is None or second_tree_el is None:
            continue
        if first_tree_el.parent.value != second_tree_el.parent.value:
            bad_nodes.add(first_tree_el.value)
            bad_nodes.add(second_tree_el.value)
            if first_tree_el.parent.value != 1:
                bad_nodes.add(first_tree_el.parent.value)
            if second_tree_el.parent.value != 1:
                bad_nodes.add(second_tree_el.parent.value)

    return bad_nodes


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




