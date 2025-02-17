
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def add_child(self, value):
        child = TreeNode(value)
        child.parent = self
        self.children.append(child)

    def __str__(self, level=0):
        result = "  " * level + f"|-- {self.value}\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def search(self, parent_val):
        if self.value == parent_val:
            return self
        for child in self.children:
            result = child.search(parent_val)
            if result:
                return result
        return None

    def delete(self, value):
        node = self.search(value)
        if node:
            for child in node.children:
                child.parent = node.parent
                node.parent.children.append(child)
            node.parent.children.remove(node)
            node.parent = None
            return True
        return False
