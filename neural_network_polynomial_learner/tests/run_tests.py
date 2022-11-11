import os

def run_unit_tests() -> None:   
    os.chdir('unit')
    os.system('pytest -q')
    os.chdir('..')


def main() -> None:
    """ Main program for testing.
    """
    run_unit_tests()

if __name__ == "__main__":
    main()