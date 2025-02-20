from custom_structure.Tree import TreeNode
from logic import input_parse, find_worst_parent, find_bad_nodes


min_deleted_answer = None


def min_deleted(tree1, tree2, node, del_count = 0):
    global min_deleted_answer
    tree1.delete(node)
    tree2.delete(node)

    bad_nodes = find_bad_nodes(len(tree1), tree1, tree2)

    if bad_nodes:
        for bad_node in bad_nodes:
            min_deleted(tree1, tree2, bad_node, del_count + 1)
    else:
        if del_count < min_deleted_answer:
            min_deleted_answer = del_count


def main():
    # m_nodes, first_tree_pairs, second_tree_pairs = input_parse()
    first_tree_pairs = [(1, 2), (2, 3), (3, 4), (4, 5)]
    second_tree_pairs = [(1, 2), (2, 3), (2, 4), (4, 5)]

    m_nodes = 5
    global min_deleted_answer
    min_deleted_answer = m_nodes

    first_tree = TreeNode(1).create_from_list(first_tree_pairs)
    second_tree = TreeNode(1).create_from_list(second_tree_pairs)
    print(first_tree)
    print(second_tree)

    bad_nodes = find_bad_nodes(m_nodes, first_tree, second_tree)
    print(bad_nodes)
    if bad_nodes:
        for bad_node in bad_nodes:
            min_deleted(first_tree, second_tree, bad_node, 1)
    else:
        min_deleted_answer = 0

    print(min_deleted_answer)


if __name__ == "__main__":
    main()
