import argparse
import sys
from typing import List
from time import sleep
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
    valid_delay_value = delay >= 0
    if(not(delay >= 0)):
        raise ValueError("ERROR: Provided an invalid delay time\n" +
                         "       Delay times must be greater than or equal to 0!")

    microwave = Microwave()

    user_input = ""
    while(not(user_input.lower() == "quit")):
        print(microwave.current_time)
        user_input = input("Please enter microwave key commands:\n")
        user_input = user_input.strip()
        print("\n")

        input_is_digit = len(user_input) == 1 and user_input.isdigit()
        if(input_is_digit):
            microwave.add_time(int(user_input))

        elif(user_input.lower() == "start"):
            while(not(microwave.current_time == "00:00")):
                print(microwave.current_time)
                microwave.count_down_one_second()
                sleep(delay)


if __name__ == "__main__":
    main()