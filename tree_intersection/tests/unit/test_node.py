import pytest
import sys
sys.path.append("../../")
from node import Node

def test_node():
#    Test Trees:
#       A            A                A
#    ┌─────┐         │                │
#    │     │         │                │
#    B   ┌─C─┐     ┌─C─┐     ─────►   C
#        │   │     │   │              │
#        │   │     │   │              │
#        E   D     F   E              E


    # Manually Construct Trees
    trees = [Node(), Node()]

    trees[0].value = "A"
    trees[0].add_child(Node())
    trees[0].children[0].value = "B"
    trees[0].add_child(Node())
    trees[0].children[1].value = "C"
    trees[0].children[1].add_child(Node())
    trees[0].children[1].children[0].value = "E"
    trees[0].children[1].add_child(Node())
    trees[0].children[1].children[1].value = "D"

    trees[1].value = "A"
    trees[1].add_child(Node())
    trees[1].children[0].value = "C"
    trees[1].children[0].add_child(Node())
    trees[1].children[0].children[0].value = "F"
    trees[1].children[0].add_child(Node())
    trees[1].children[0].children[1].value = "E"

    # Test tree construction via dictionary
    tree_0_dict = {"A" :
                      {"B" : "Leaf",
                       "C" : 
                          {"E" : "Leaf",
                           "D" : "Leaf"
                          }
                      }
                  }
    assert(trees[0] == Node.init_from_dict(tree_0_dict))

    # Test intersection method
    expected_intersection_dict = {"A" :
                                     {"C" : 
                                        {"E" : "Leaf"
                                        }
                                     }
                                 }
    expected_intersection = Node.init_from_dict(expected_intersection_dict)
    intersection = trees[0].intersection(trees[1])
    assert(intersection == expected_intersection)

    # Test to_dict method
    assert(intersection.to_dict() == expected_intersection_dict)