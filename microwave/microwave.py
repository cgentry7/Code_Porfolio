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

    Attributes
    ----------
    current_time : str
        A string representation of the current time stored in the microwave timer
        using the "00:00" format
    """

    @property
    def current_time(self) -> str:
        pass

    def __init__(self) -> None:

    def add_time(self, digit: int) -> None:
        pass

    def count_down_one_second(self) -> None:
        pass