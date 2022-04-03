__version__ = '0.1.0'

from graph import Node


def find_most_flexible_path(node: Node, path: list[Node] = [], count: int = 0):
    if len(node.choices) == 0:
        return path + [node], count
    option_paths = [find_most_flexible_path(n, path + [node], count + len(node.choices)) for n in node.choices]

    return max(*option_paths, key=lambda pc: pc[1])
