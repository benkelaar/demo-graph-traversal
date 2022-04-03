from __future__ import annotations


class AdaptationNode:
    """Node that fully describes a graph of adaptation pathways.

    Recursively contains all possible downstream choices.
    """

    def __init__(self, node_id: str, choices: list[AdaptationNode] = None):
        self.node_id = node_id
        self.choices = [] if choices is None else choices

    def choice_count(self):
        return len(self.choices)

    def is_leaf_node(self):
        return self.choice_count() == 0

    def __str__(self):
        choice_description = ("leaf" if self.is_leaf_node() else
                              "1 choice" if self.choice_count() < 2 else
                              f"{self.choice_count()} choices")
        return f"Node['{self.node_id}', {choice_description}]"


AdaptationPath = list[AdaptationNode]
