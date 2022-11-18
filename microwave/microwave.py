from __future__ import annotations

class Microwave(object):
    """ A class which mimics a microwave interface

    Though this class could be made more flexible, I have designed it to
    strictly adhere to the behavior of a simple microwave interface.  So,
    the client may only set the timer by adding non-negative numbers one
    digit at a time, may query the current time as a string, and may decrement
    the timer by one second using the appropriate method.

    There are myriad different getters and setters we could give clients 
    to expose greater power over these objects, but as a means of defensive
    programming, I will, for the time being, explicitly limit the current
    accessibility of the class methods.

    There are almost certainly better ways to store this rather than
    a Python list, but I'm trying not to spend an excessive amount of time on
    design and just do what I can quickly come up with first.

    Attributes
    ----------
    current_time : str
        A string representation of the current time stored in the microwave timer
        using the "00:00" format
    """

    @property
    def current_time(self) -> str:
        return "{}{}:{}{}".format(self._time[3], self._time[2],
                                  self._time[1], self._time[0])

    def __init__(self) -> None:
        self._time = [0]*4

    def add_time(self, entry: int) -> None:
        """ Method to add an entry to the timer

        Will do nothing if self._time is already full (i.e. all 4 digits are occupied by a number)

        Parameters
        ----------
        entry : int
            The number to be added to the microwave timer
        """
        assert(entry >= 0 and entry < 10)

        timer_full = self._time[-1] > 0
        if(timer_full):
            return
        
        for i in range(len(self._time)-1, 0 , -1):
            self._time[i] = self._time[i-1]
        self._time[0] = entry


    def count_down_one_second(self) -> None:
        """ Method to decriment the timer by one second

        There is almost certainly a more clever way to do this that minimizes
        the number of if-statements at play.  I'm imagining something involving
        modulus operations.  However, I'm trying to keep my implementation time
        within roughly 1 hr, so I didn't go for perfect here...
        """

        minus_one = True
        for i in range(len(self._time)):
            if minus_one:
                minus_one = False
                if self._time[i] == 0 and any([digits > 0 for digits in self._time[i:]]):
                    is_a_minute_turn_over = i == 1
                    if is_a_minute_turn_over:
                        self._time[i]   = 5
                        self._time[i-1] = 9
                    else:
                        self._time[i] = 9
                    minus_one = True
                elif self._time[i] > 0:
                    self._time[i] -= 1