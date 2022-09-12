# Tree Intersection

A Python code for performing a basic tree intersection as part of a coding challenge problem

Version / Module Requirements
-----------------------------
- Written using Python 3.10.6
- Pytest module required for execution of unit tests

User Instructions
------------------
For command line execution, the user may call the main program `tree_intersection.py` along with an input file:
```
python tree_intersection.py -i <input_file>
```
This will produce an output file `output.json` which has the intersection of the two given trees in the input file.

The input and output files represent the trees using JSON format.  For the case below:
```
   A            A                A
┌─────┐         │                │
│     │         │                │
B   ┌─C─┐     ┌─C─┐     ─────►   C
    │   │     │   │              │
    │   │     │   │              │
    E   D     F   E              E
```

The input file would be:
```
[
    {"A" :
        {"B" : "Leaf",
         "C" : 
            {"E" : "Leaf",
             "D" : "Leaf"
            }
        }
    },

    {"A" :
        {"C" :
            {"F" : "Leaf",
             "E" : "Leaf"
            }
        }
    }
]
```

and the resulting output file:
```
{
    "A": {
        "C": {
            "E": "Leaf"
        }
    }
}
```

To run the unit & verification tests, simply execute the following from the `tests` folder:
```
python run_tests.py
```

Requirements
----------------------
1. Return the intersection of two given (not necessarily binary) trees
    - Intersection - all paths from the root node in your final tree should be valid paths from the root nodes in the original trees
2. Make a data structure that can represent trees
3. Provide a print function that can help verify the solutions


Solution Design
---------------
- The `Node` class will provide a data structure with which one might represent such trees.  It will have the attribute `value` to represent the node value and `children` to represent the child nodes of a given node.  (Satisfies Requirement 2)
- The `Node` class will also have an `intersection` method which will return the intersection between a node (i.e. the tree it represents) and some other node.  A `Node` Module free function will be made available for the main program in `tree_intersection.py` to use. (Satisfies Requirement 1)
- The `Node` class will also have a `to_dict` method which will return a dictionary representation of the `Node`.  This will then be cast into JSON format and output to the `output.json` file via the main function in `tree_intersection.py`. (Satisfies Requirement 3)