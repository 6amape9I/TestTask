from __future__ import annotations

from graphviz import Digraph


class Graph:

    def __init__(self, value: int):
        self.value = value
        self.neighbors = set()

    def __str__(self):
        return str(self.value)

    def add(self, neighbor_value: int):
        neighbor = self.graph_search(neighbor_value)
        if isinstance(neighbor, int):
            neighbor = Graph(neighbor_value)
        self.neighbors.add(neighbor)
        neighbor.neighbors.add(self)
        return self

    def graph_search(self, value: int) -> Graph | int:
        visited = []
        stack = [self]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                if current.value == value:
                    return current
                stack.extend(current.neighbors)
        return value

    def create_from_list(self, pairs_list):
        for pair in pairs_list:
            graph = self.graph_search(pair[0])
            if isinstance(graph, int):
                graph = Graph(pair[0])
            graph.add(pair[1])
        return self

    def save_graph(self, filename='graph'):
        dot = Digraph()
        visited = set()

        def add_nodes_edges(node):
            if node is None or node.value in visited:
                return
            visited.add(node.value)
            dot.node(str(node.value))
            for child in node.neighbors:
                dot.edge(str(node.value), str(child.value))
                add_nodes_edges(child)

        add_nodes_edges(self)
        dot.render(filename, format="jpg", cleanup=True)
        return self