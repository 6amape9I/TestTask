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





