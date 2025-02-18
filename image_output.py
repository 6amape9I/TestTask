from graphviz import Digraph
def save(root, highlight_node=1, filename='tree'):
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
    dot.render(filename, cleanup=True)
    print(f"Визуализация сохранена в файл {filename}.png")