from custom_structure.Tree import TreeNode
from logic import find_bad_nodes

min_deleted_list = []
m_nodes = 0

def min_deleted(tree1, tree2, node_val, del_list=None):
    if del_list is None:
        del_list = set()
    global min_deleted_list
    global m_nodes
    tree1.delete(node_val)
    tree2.delete(node_val)

    bad_nodes = find_bad_nodes(m_nodes, tree1, tree2)

    if bad_nodes:
        for bad_node in bad_nodes:
            del_list.add(bad_node)
            min_deleted(tree1, tree2, bad_node, del_list)
    else:
        if len(del_list) < len(min_deleted_list):
            min_deleted_list = del_list


def main():
    # m_nodes, first_tree_pairs, second_tree_pairs = input_parse()
    first_tree_pairs = [(1, 2), (1, 4), (1, 7), (2, 12), (2, 3),
                        (3, 10), (4, 11), (4, 5), (4, 14),
                        (5, 9), (5, 15), (7, 8), (7, 6),
                        (8, 13)]
    second_tree_pairs = [(1, 6), (1, 2), (1, 13), (1, 7),
                         (6, 3), (3, 4), (3, 5),
                         (2, 11), (2, 8), (13, 12),
                         (13, 15), (13, 10),
                         (7, 14), (14, 9)]
    max_nodes = 15


    global min_deleted_list
    min_deleted_list = list(range(1, max_nodes + 1))
    global m_nodes
    m_nodes = max_nodes

    first_tree = TreeNode(1).create_from_list(first_tree_pairs)
    second_tree = TreeNode(1).create_from_list(second_tree_pairs)
    print(first_tree)
    print(second_tree)

    bad_nodes = find_bad_nodes(m_nodes, first_tree, second_tree)
    print(bad_nodes)
    if bad_nodes:
        for bad_node in bad_nodes:
            del_list = set()
            del_list.add(bad_node)
            min_deleted(first_tree, second_tree, bad_node, del_list)
    else:
        min_deleted_list = []

    print(min_deleted_list)


if __name__ == "__main__":
    main()
