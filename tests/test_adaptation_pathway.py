from adaptation_pathway import AdaptationNode


def test_leaf_node():
    leaf_node = AdaptationNode("leaf")
    assert leaf_node.choice_count() == 0
    assert leaf_node.is_leaf_node()


def test_root_node():
    root_node = AdaptationNode("root", [AdaptationNode("leaf1"), AdaptationNode("leaf2")])
    assert root_node.choice_count() == 2
    assert not root_node.is_leaf_node()


def test_string_representation():
    leaf_node = AdaptationNode("leaf1")
    continuation = AdaptationNode("cont", [AdaptationNode("leaf2")])
    root_node = AdaptationNode("root", [leaf_node, continuation])
    assert str(root_node) == "Node['root', 2 choices]"
    assert str(leaf_node) == "Node['leaf1', leaf]"
    assert str(continuation) == "Node['cont', 1 choice]"
