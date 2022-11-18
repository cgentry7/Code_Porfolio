import os
import filecmp

VERIFICATION_TESTS = ["basic_test"]

def run_unit_tests() -> None:   
    os.chdir('unit')
    os.system('pytest -q')
    os.chdir('..')


def run_verification_tests() -> None:
    failed_test = []
    os.chdir('verification')
    for test in VERIFICATION_TESTS:
        os.chdir(test)
        os.system('echo "$(cat input.txt)" | python ../../../run_microwave.py > output.txt')
        if os.path.exists("./output.txt"):
            if not(filecmp.cmp("./output.txt", "./gold/output.txt")):
                failed_test.append(test)
        else:
            failed_test.append(test)
        os.chdir('..')
    os.chdir('..')
    if failed_test:
        print("Tests Failed")
        print("------------")
        for test in failed_test:
            print(test)
    else:
        print("All Tests Passed!")


def main() -> None:
    """ Main program for testing run_microwave.py

        This is a very lightweight testing framework meant to
        provide very basic unit and verification testing.  Normally
        I would like more details on how things failed, along with automated
        rebasing.
    """
    run_unit_tests()
    run_verification_tests()

if __name__ == "__main__":
    main()