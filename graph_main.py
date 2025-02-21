from custom_structure.Graph import Graph


def delete_update(value, graph_edges):
    graph_edges = new_edges(graph_edges, value)
    sorted(graph_edges, key=lambda x: x[0])
    graph = Graph(1).create_from_list(graph_edges)
    return graph, graph_edges


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
    max_cycle = 0

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
    minimum_val = 1000000
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


def main():
    # m_nodes, first_tree_pairs, second_tree_pairs = input_parse()
    first_tree_pairs = [(1, 2), (2, 3), (3, 4), (4, 5)]
    second_tree_pairs = [(1, 2), (2, 3), (2, 4), (4, 5)]
    m_nodes = 5

    graph_root = Graph(1)
    graph_edges = first_tree_pairs
    for pair in second_tree_pairs:
        if pair not in graph_edges:
            graph_edges.append(pair)
    graph = graph_root.create_from_list(graph_edges)

    cycles = find_all_cycles(graph)

    while cycles:
        for cycle in cycles:
            all_possible, mins = count_transitive_edges(cycle, graph_edges)
            print("All possible: ", all_possible)
            print("Mins: ", mins)
            for min_val in mins:
                graph, graph_edges = delete_update(min_val, graph_edges)
                print("Graph edges: ", graph_edges)
                print("Graph: ", graph)
        cycles = find_all_cycles(graph)


if __name__ == "__main__":
    main()
