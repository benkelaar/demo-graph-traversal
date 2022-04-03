from adaptation_pathway import AdaptationNode
from graph_traversal import find_most_flexible_path


def test_no_path():
    root = AdaptationNode("root")
    assert find_most_flexible_path(root) == ([root], 0)


def test_simple_path():
    choice1 = AdaptationNode("1")
    root = AdaptationNode("root", [choice1, AdaptationNode("2")])
    assert find_most_flexible_path(root) == ([root, choice1], 2)


def test_more_complex_path():
    choice1 = AdaptationNode("1", [AdaptationNode("1a"), AdaptationNode("1b")])
    choice2a = AdaptationNode("2a")
    choice2 = AdaptationNode("2", [choice2a, AdaptationNode("2b"), AdaptationNode("2c")])
    root = AdaptationNode("root", [choice1, choice2])
    assert find_most_flexible_path(root) == ([root, choice2, choice2a], 5)
