from custom_structure.Tree import TreeNode
from logic import input_parse, find_worst_parent


def main():
    # m_nodes, first_tree_pairs, second_tree_pairs = input_parse()
    first_tree_pairs = [(1, 2), (2, 3), (3, 4), (4, 5)]
    second_tree_pairs = [(1, 2), (2, 3), (2, 4), (4, 5)]
    m_nodes = 5

    first_tree = TreeNode(1).create_from_list(first_tree_pairs)
    second_tree = TreeNode(1).create_from_list(second_tree_pairs)
    print(first_tree)
    print(second_tree)
    check = first_tree == second_tree
    print(check)

    while first_tree != second_tree:
        worst_parent = find_worst_parent(m_nodes, first_tree, second_tree)
        print(worst_parent)

        first_tree.delete(worst_parent)
        second_tree.delete(worst_parent)
        print(first_tree)
        print(second_tree)
        check = first_tree == second_tree
        print(check)

    answer = m_nodes - len(first_tree)
    print(answer)


if __name__ == "__main__":
    main()

