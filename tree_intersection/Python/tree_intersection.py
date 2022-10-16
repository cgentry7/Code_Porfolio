import argparse
import json
import sys
from typing import List
from node import Node

def parse_arguments(arguments: List[str]) -> argparse.Namespace:
    """ A command line parser

    Parameters
    ----------
    arguments : List[str]
        The command line arguments

    Returns
    -------
    argparse.Namespace
        The argparse.Namespace made using the command line arguments
    """
    
    if arguments is None: arguments = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", action="store", help="The input JSON file")
    return parser.parse_args(arguments)


def main(arguments: List[str]=None) -> None:
    """ The main function for this program

    Parameters
    ----------
    arguments : List[str]
        The command line arguments
    """
    input_file = parse_arguments(arguments).input_file

    trees = []
    with open(input_file) as json_file:
        json_data = json.load(json_file)
        for i in [0, 1]:
            try:
                trees.append(Node.init_from_dict(json_data[i]))
            except:
                raise SyntaxError("JSON input parsing failed\n" +
                                  "See verification tests for examples of valid JSON inputs")
        
    intersection = trees[0].intersection(trees[1])

    with open("output.json", "w") as output_file:
        json.dump(intersection.to_dict(), output_file, indent = 4)
    

if __name__ == "__main__":
    main()