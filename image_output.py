from pathlib import Path

from graphviz import Digraph
import cv2


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


def video_create(path="img"):
    path = Path(path)
    img = path.glob('*.jpg')
    img_sorted = sorted(img, key=lambda x: int(x.stem.split('_')[-1]))
    img_sorted = [cv2.imread(str(f)) for f in img_sorted]

    height, width, layers = img_sorted[0].shape
    output_name = path.parent / f'{path.name}.avi'
    output_name = r'' + str(output_name)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 1
    video = cv2.VideoWriter(output_name, fourcc, fps, (width, height))

    for img in img_sorted:
        image = cv2.resize(img, (width, height))
        video.write(image)

    video.release()
