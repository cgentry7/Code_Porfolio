import argparse
import sys
from typing import List
from microwave import Microwave

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
    parser.add_argument("-d", "--delay", action="store", default=0, type=int, help="The time delay in seconds between each second during the microwave countdown")
    return parser.parse_args(arguments)


def main(arguments: List[str]=None) -> None:
    """ The main function for this program

    Parameters
    ----------
    arguments : List[str]
        The command line arguments
    """
    delay = parse_arguments(arguments).delay

   

if __name__ == "__main__":
    main()