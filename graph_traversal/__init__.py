__version__ = '0.1.0'

from adaptation_pathway import AdaptationNode, AdaptationPath


def find_most_flexible_path(
        node: AdaptationNode,
        pathway: AdaptationPath = None,
        flexibility: int = 0
) -> tuple[AdaptationPath, int]:
    """Find the most flexible decision path through an adaptation pathway, as defined by the passed in AdaptationNode.

    The "most flexible" is defined in this instance as the pathway that "sees" the greatest variation
    of possible choices.

    For equal flexibilities the algorithm is stable, so should return the first found path with that flexibility.

    :param node: root node for the path to test for flexibility
    :param pathway: path taken so far, defaults to `[current_node]`
    :param flexibility: Amount of choices seen so far, defaults to 0
    :return: a pair of the first most flexible path seen and its total flexibility
    """

    followed_path = [node] if pathway is None else pathway + [node]
    # Exit condition
    if node.is_leaf_node():
        return followed_path, flexibility

    # Otherwise, recurse for all available choices
    new_flexibility = flexibility + node.choice_count()
    choice_path_flexibilities = map(lambda new_node: find_most_flexible_path(new_node, followed_path, new_flexibility),
                                    node.choices)

    # And select first tuple with the highest flexibility count
    return max(choice_path_flexibilities, key=lambda pf_pair: pf_pair[1])
