class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def generate_trees(n):
    if n == 0:
        return []
    if n == 1:
        return [TreeNode(1)]

    all_trees = []
    for root_value in range(1, n + 1):
        left_trees = generate_trees(root_value - 1)
        right_trees = generate_trees(n - root_value)

        for left in left_trees:
            for right in right_trees:
                root = TreeNode(root_value)
                root.add_child(left)
                root.add_child(right)
                all_trees.append(root)

    return all_trees


# Пример использования
n = 5
trees = generate_trees(n)
print(trees[0])
print(trees[1])
print(f"Сгенерировано {len(trees)} деревьев для n={n}.")
