from custom_structure.Tree import TreeNode


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

    print(worst_parent)

    if worst_parent == 1:
        worst_parent = 0
        trees_values = set([el.value for el in first_tree.children + second_tree.children])
        for el in trees_values:
            if bad_parents[el] > bad_parents[worst_parent]:
                worst_parent = el
        return worst_parent

    if worst_parent == 0:
        return False

    return worst_parent


def main():
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
    print(first_tree_pairs)
    print(second_tree_pairs)
    print(m_nodes)

    first_tree = TreeNode(1).create_from_list(first_tree_pairs)
    second_tree = TreeNode(1).create_from_list(second_tree_pairs)

    print(first_tree)
    print(second_tree)

    worst_parent = 32
    deleted = 0

    while worst_parent:
        worst_parent = find_worst_parent(m_nodes, first_tree, second_tree)
        print(worst_parent)
        first_tree.delete(worst_parent)
        second_tree.delete(worst_parent)
        deleted += 1

        print(first_tree)
        print(second_tree)

    answer = m_nodes - deleted
    print(answer)


if __name__ == "__main__":
    main()
