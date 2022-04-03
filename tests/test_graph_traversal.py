from graph import Node
from graph_traversal import __version__, find_most_flexible_path


def test_version():
    assert __version__ == '0.1.0'


def test_no_path():
    root = Node("root")
    assert find_most_flexible_path(root) == ([root], 0)


def test_simple_path():
    choice1 = Node("1")
    root = Node("root", [choice1, Node("2")])
    assert find_most_flexible_path(root) == ([root, choice1], 2)


def test_more_complex_path():
    choice1 = Node("1", [Node("1a"), Node("1b")])
    choice2a = Node("2a")
    choice2 = Node("2", [choice2a, Node("2b"), Node("2c")])
    root = Node("root", [choice1, choice2])
    assert find_most_flexible_path(root) == ([root, choice2, choice2a], 5)
