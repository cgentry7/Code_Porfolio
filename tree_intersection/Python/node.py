from __future__ import annotations
from typing import List, Dict

class Node(object):
    """ A tree node along with its children

    This is the base class from which tree structures can be built

    This probably could have used a full composite pattern, but we're just
    going to use a simplified form of that here

    Attributes
    ----------
    value : str
        The value of the Node
    children : List[Node]
        The children of the Node
    is_leaf : bool
        Indicator of whether or not a Node is a Leaf (i.e. has no children)
    """

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    @property
    def children(self) -> List[Node]:
        return self._children
    
    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def __init__(self) -> None:
        self._value = ""
        self._children = []

    def init_from_dict(input_dict: Dict) -> Node:
        """ Initializes a node using a dictionary to build out its tree structure

        Parameters
        ----------
        input_dict : Dict
            The dictionary with which to full construct the node and its children
        """
        assert(isinstance(input_dict, dict))
        assert(len(input_dict) == 1)
        node = Node()
        for key, value in input_dict.items():
            assert(isinstance(key, str))
            assert(isinstance(value, dict) or isinstance(value, str))
            node.value = key
            if isinstance(value, dict):
                for child_key, child_value in value.items():
                    node.children.append(Node.init_from_dict({child_key : child_value}))
            if isinstance(value, str):
                assert(value == "Leaf")
        return node

    def __eq__(self, other: Node) -> bool:
        """ Checks for equality between two nodes

        Parameters
        ----------
        other : Node
            The other node to compare against
        """
        # There are probably more efficient ways to do this
        # but I figure I can leverage the already extant dictionary
        # comparison, and revist this if it proves too slow
        return (self.to_dict() == other.to_dict())

    def add_child(self, child: Node) -> None:
        """  Adds a child node

        Parameters
        ----------
        child : Node
            The child node to be added
        """
        self._children.append(child)

    def intersection(self, other: Node) -> Node:
        """ Determine the intersection of the node tree structure and some other node tree structure

        This implementation is loosely inspired by this post:
        https://stackoverflow.com/questions/62493961/algorithm-for-finding-equal-paths-in-two-trees

        Parameters
        ----------
        other : Node
            The other node tree structure to compare against for the intersection
        
        Returns
        -------
        Node
            The intersection of the two node trees structures
        """
        node = Node()
        if self.value == other.value:
            if self.is_leaf and other.is_leaf:
                node.value = self.value
            else:
                intersecting_children = []
                for self_child in self.children:
                    for other_child in other.children:
                        intersection_node = self_child.intersection(other_child)
                        children_intersect = not(intersection_node.value == "")
                        if children_intersect:
                            intersecting_children.append(intersection_node)
                if len(intersecting_children) > 0:
                    node.value = self.value
                    for child in intersecting_children:
                        # This prevents repeating intersections if they're already accounted for
                        if any([child == other_child for other_child in node.children]):
                            continue
                        node.children.append(child)
        return node

    def to_dict(self) -> Dict:
        """ Returns the node tree structure as a Python dictionary

        Returns
        ----------
        Dict
            The dictionary form of the node tree structure
        """
        output_dict = {}
        if not(self.value == ""):
            key = self.value
            if self.is_leaf:
                output_dict[key] = "Leaf"
            else:
                value = {}
                for child in self.children:
                    child_dict = child.to_dict()
                    for child_key, child_value in child_dict.items():
                        value[child_key] = child_value 
                output_dict[key] = value
        assert(len(output_dict) == 0 or len(output_dict) == 1)
        return output_dict

    