from custom_structure.Tree import TreeNode


def main():

    max_nodes = int(input())
    first_tree_pairs = []
    second_tree_pairs = []

    _ = input()

    for _ in range(max_nodes - 1):
        first_tree_pairs.append(tuple(map(int, input().split())))

    _ = input()

    for _ in range(max_nodes - 1):
        second_tree_pairs.append(tuple(map(int, input().split())))

    first_tree = TreeNode(first_tree_pairs[0][0])
    for pair in first_tree_pairs:
        parent_val, child_val = pair
        parent = first_tree.search(parent_val)
        parent.add_child(child_val)


    print(first_tree)

    second_tree = TreeNode(second_tree_pairs[0][0])
    for pair in second_tree_pairs:
        parent_val, child_val = pair
        parent = second_tree.search(parent_val)
        parent.add_child(child_val)

    print(second_tree)










if __name__ == "__main__":
    main()