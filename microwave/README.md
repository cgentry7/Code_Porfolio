# Microwave

A code for simulating the behavior of a simple microwave

User Instructions
------------------
To run this code, users should execute the following command line statement:

```
python run_microwave.py
```

This command also has an optional argument for the countdown delay `-d` or `--delay` which dictates how long in seconds
the code will pause between each second during the microwave countdown.  The default value is `1`.

Upon executing the above command, the program will prompt the user to enter microwave-interface-like commands as shown below:

```
Please enter microwave key commands:
```

Users may then provide single entry commands in a manner analogous to the operations of a normal microwave display.
This code expects either non-negative integer values less than 10, the keyword `START` (case-insensitive) which
will start the microwave count down, or the keyword `QUIT` (case-insensitive) which will terminate the program.
The program will echo the countdown to the screen until the timer runs out, at which point the program will await new commands.
Invalid commands will simply be ignored. An example of the expected behavior is provided below:

```
python run_microwave.py

00:00
Please enter microwave key commands:
1


00:01
Please enter microwave key commands:
0


00:10
Please enter microwave key commands:
3


01:30
Please enter microwave key commands:
START


01:30
01:29
01:28
.
.
.
00:03
00:02
00:01
00:00
Please enter microwave key commands:
QUIT
```

To run the unit tests, simply execute the following from the `tests` folder:
```
python run_tests.py
```

Requirements
----------------------
1. Design and Implement a software interface that mimics the interface of a microwave oven
2. Design need only accept single digit non-negative numbers and a _START_ command
3. Use print statements for user feedback
4. Print what the display will show after each number press
5. While cooking, print what the display will show after every second until completed
6. Once cooking has completed, it's OK to display either "00:00" or "DONE"
7. The original state of the display is "00:00"
8. The maximum allowed time is "99:99"
9. The display cannot be turned off/on or cleared


Solution Design
---------------
- `microwave.py` has a `Microwave` class which has a timer, a method for adding time to the timer `add_time` which takes single digit non-negative integers and appends the timer in a manner which mimics a typical microwave, a method for decreasing the timer by one second `count_down_one_second`, and a method for getting a string representation of the current time condition `current_time`.  A `Microwave` object timer initializes with a timer of "00:00" and can go up to "99:99", as is enforced by the `add_time` interface (Satisfies Requirement 1 & 9).
- `run_microwave.py` enforces the interface constrainted via the UI (Satisfies Requirement 2 & 9)
- `run_microwave.py` prints the appropriate user feedback (Satisfies Requirement 3)
- `run_microwave.py` prints the current time after every button press using the `current_time` method of the operable `Microwave` object (Satisfies Requirement 4)
- `run_microwave.py` prints the current time during "cooking" using the `current_time` method of the operable `Microwave` object.  Cooking consists of `run_microwave.py` repeatedly calling `count_down_one_second` until the timer is back to "00:00" (Satisfies Requirement 5 & 6)
- `run_microwave.py` will display a freshly initialized `Microwave` timer on start (Satisfies Requirement 7)


