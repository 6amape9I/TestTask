from graphviz import Digraph


class TreeNode:

    def __init__(self, value: int):
        self.value = value
        self.parent = None
        self.children = []

    def __eq__(self, other: 'TreeNode'):
        if self.value != other.value:
            return False

        self_set = set(
            [child.value for child in self.children]
        )
        other_set = set(
            [child.value for child in other.children]
        )

        if self_set != other_set:
            return False

        for child in self.children:
            if child not in other.children:
                return False
        return True

    def __str__(self, level=0):
        result = "  " * level + f"|-- {self.value}\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def __hash__(self):
        return hash(self.value)

    def __len__(self):
        return 1 + sum([len(child) for child in self.children])

    def add_child(self, value):
        child = TreeNode(value)
        child.parent = self
        self.children.append(child)

    def create_from_list(self, pairs):
        for pair in pairs:
            parent_val, child_val = pair
            parent = self.search(parent_val)
            parent.add_child(child_val)
        return self

    def search(self, parent_val):
        if self.value == parent_val:
            return self
        for child in self.children:
            result = child.search(parent_val)
            if result:
                return result
        return None

    def get_all_nodes(self):
        nodes = []
        if self is None:
            return nodes
        stack = [self]
        while stack:
            node = stack.pop()
            nodes.append(node)
            for child in reversed(node.children):
                stack.append(child)
        return nodes

    def delete(self, value):
        node = self.search(value)
        if node:
            for child in node.children:
                child.parent = node.parent
                node.parent.children.append(child)
            node.parent.children.remove(node)
            node.parent = None
            return self
        return False

    def __copy__(self):
        new_tree = TreeNode(self.value)
        new_tree.parent = self.parent
        new_tree.children = [child.__copy__() for child in self.children]
        return new_tree

    def copy(self):
        new_tree = TreeNode(self.value)
        new_tree.parent = self.parent
        new_tree.children = [child.copy() for child in self.children]
        return new_tree

    def get_edges(self ):
        edges = []
        if self is None:
            return edges
        stack = [self]
        while stack:
            node = stack.pop()
            for child in node.children:
                edges.append((node.value, child.value))
                stack.append(child)
        return edges

    def delete_list(self, values):
        for value in values:
            self.delete(value)
        return self

    def save(root, highlight_node=None, filename='tree'):
        dot = Digraph()
        visited = set()

        def add_nodes_edges(node):
            if node is None or node.value in visited:
                return
            visited.add(node.value)
            # Подсвечиваем худшего родителя
            if node.value == highlight_node:
                dot.node(str(node.value), color='red', style='filled', fillcolor='pink')
            else:
                dot.node(str(node.value))
            for child in node.children:
                dot.edge(str(node.value), str(child.value))
                add_nodes_edges(child)

        add_nodes_edges(root)
        dot.render(filename, format="jpg", cleanup=True)