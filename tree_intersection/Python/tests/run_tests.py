import os
import filecmp

VERIFICATION_TESTS = ["coding_challenge_example",
                      "different_levels",
                      "no_match",
                      "repeat_values",
                      "repeat_intersect_branches"]

#VERIFICATION_TESTS = ["coding_challenge_example",
#                      "different_levels",
#                      "no_match",
#                      "repeat_values"]

def run_unit_tests() -> None:   
    os.chdir('unit')
    os.system('pytest -q')
    os.chdir('..')


def run_verification_tests() -> None:
    failed_test = []
    os.chdir('verification')
    for test in VERIFICATION_TESTS:
        os.chdir(test)
        os.system('python ../../../tree_intersection.py -i input.json')
        if os.path.exists("./output.json"):
            if not(filecmp.cmp("./output.json", "./gold/output.json")):
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
    """ Main program for testing tree_intersection.py

        This is a very lightweight testing framework meant to
        provide very basic unit and verification testing.  Normally
        I would like more details on how things failed, along with automated
        rebasing.
    """
    run_unit_tests()
    run_verification_tests()

if __name__ == "__main__":
    main()