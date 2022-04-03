from __future__ import annotations


__version__ = '0.1.0'


class Node:
    def __init__(self, node_id: str, choices: list[Node] = []):
        self.node_id = node_id
        self.choices = choices

    def __str__(self):
        return f"{self.node_id}, {len(self.choices)} options"
