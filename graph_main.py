from custom_structure.Graph import Graph
from image_output import video_create
from logic import (different_in_list, find_all_cycles, count_val_in_cycles, count_transitive_edges, delete_update,
                   input_parse)

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
    graph.save_graph(filename=f'img/graph/graph_{photo_counter}')
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

        graph.save_graph(filename=f'img/graph/graph_{photo_counter}')
        photo_counter += 1

        print("_______________________________________")
        print("Graph edges: ", graph_edges)
        differ = different_in_list(first_tree_pairs, second_tree_pairs)
        cycles = find_all_cycles(graph)

    differ = different_in_list(first_tree_pairs, second_tree_pairs)
    print("Different: ", differ)

    print("Answer: ", len(deleted))
    print("Deleted: ", deleted)

    graph.save_graph(filename=f'img/graph/graph_{photo_counter}')
    photo_counter += 1

    return len(deleted)


if __name__ == "__main__":
    graph_main()
    video_create(path="img/graph")
