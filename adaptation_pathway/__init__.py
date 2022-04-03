from __future__ import annotations


class AdaptationNode:
    def __init__(self, node_id: str, choices=None):
        self.node_id = node_id
        self.choices = [] if choices is None else choices

    def choice_count(self):
        return len(self.choices)

    def is_leaf_node(self):
        return self.choice_count() == 0

    def __str__(self):
        return f"Node['{self.node_id}', {self.choice_count()} choices]"


AdaptationPath = list[AdaptationNode]
