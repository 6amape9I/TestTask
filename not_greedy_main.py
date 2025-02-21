from custom_structure.Tree import TreeNode
from logic import input_parse


def node_list_generator(m_nodes):
    bit_mask = 0
    list = [i for i in range(2, m_nodes + 1)]
    while bit_mask != (2 ** (m_nodes - 1)) - 1:
        yield [list[i] for i in range(m_nodes) if bit_mask & (1 << i)]
        bit_mask += 1


def not_greedy_main(m_nodes=0, first_tree_pairs=None, second_tree_pairs=None):
    #m_nodes, first_tree_pairs, second_tree_pairs = input_parse()
    list_gen = node_list_generator(m_nodes)

    first_tree = TreeNode(1).create_from_list(first_tree_pairs)
    second_tree = TreeNode(1).create_from_list(second_tree_pairs)

    answer_list = []
    min_len = 16

    for i in range(1, 2 **(m_nodes - 1)):
        new_list = next(list_gen)
        if len(new_list) > min_len:
            continue
        first_tree.delete_list(new_list)
        second_tree.delete_list(new_list)
        if first_tree == second_tree and len(new_list) <= min_len:
            print("Found: ", new_list)
            answer_list.append(new_list)
            min_len = len(new_list)
        first_tree = TreeNode(1).create_from_list(first_tree_pairs)
        second_tree = TreeNode(1).create_from_list(second_tree_pairs)

    min_answer = min(answer_list, key=len)
    print(min_answer)
    return min_answer


if __name__ == "__main__":
    not_greedy_main()
