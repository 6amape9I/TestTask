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