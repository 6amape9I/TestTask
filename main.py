from custom_structure.Tree import TreeNode
from image_output import video_create
from logic import input_parse, find_worst_parent


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
    m_nodes = 15

    first_tree = TreeNode(1).create_from_list(first_tree_pairs)
    second_tree = TreeNode(1).create_from_list(second_tree_pairs)

    worst_parent = 32
    deleted = 0
    photo_counter = 0

    first_tree.save(filename=f'img/first/tree_{photo_counter}')
    second_tree.save(filename=f'img/second/tree_{photo_counter}')
    photo_counter += 1
    deleted = []

    while worst_parent:
        worst_parent = find_worst_parent(m_nodes, first_tree, second_tree)
        deleted.append(worst_parent)

        first_tree.save(filename=f'img/first/tree_{photo_counter}')
        second_tree.save(filename=f'img/second/tree_{photo_counter}')
        photo_counter += 1

        first_tree.delete(worst_parent)
        second_tree.delete(worst_parent)

        first_tree.save(filename=f'img/first/tree_{photo_counter}')
        second_tree.save(filename=f'img/second/tree_{photo_counter}')
        photo_counter += 1

    answer = len(deleted) - 1
    print("Answer: ", answer)
    print("Deleted: ", deleted)


if __name__ == "__main__":
    main()
    video_create(path="img/first")
    video_create(path="img/second")
