import pytest
import sys
sys.path.append("../../")
from microwave import Microwave

def test_microwave():

    microwave = Microwave()
    assert(microwave.current_time == "00:00")

    #Test ignoring an initial zero
    microwave.add_time(0)
    assert(microwave.current_time == "00:00")

    #Test adding more time to the first digit
    microwave.add_time(2)
    assert(microwave.current_time == "00:02")

    #Test adding more time to the second digit
    microwave.add_time(0)
    assert(microwave.current_time == "00:20")

    #Test adding more time to the third digit
    microwave.add_time(0)
    assert(microwave.current_time == "02:00")

    #Test adding more time to the fourth digit
    #NOTE: this could fail if we failed to ignore the initial zero entry.
    #      The failure would be a reported time of 02:00, when it should be 20:00
    microwave.add_time(0)
    assert(microwave.current_time == "20:00")

    #Test to make sure users can't add more numbers once the timer is "full"
    microwave.add_time(9)
    assert(microwave.current_time == "20:00")

    #Test the countdown method (also tests the second minute digit turnover)
    microwave.count_down_one_second()
    assert(microwave.current_time == "19:59")

    #Test the first minute digit turnover
    microwave = Microwave()
    microwave.add_time(9)
    microwave.add_time(0)
    microwave.add_time(0)
    microwave.count_down_one_second()
    assert(microwave.current_time == "08:59")

    #Test the second second digit turnover
    microwave = Microwave()
    microwave.add_time(4)
    microwave.add_time(0)
    microwave.count_down_one_second()
    assert(microwave.current_time == "00:39")

    #Ensure countdown does nothing when the timer is already at 00:00
    microwave = Microwave()
    microwave.add_time(1)
    microwave.count_down_one_second()
    assert(microwave.current_time == "00:00")
    microwave.count_down_one_second()
    assert(microwave.current_time == "00:00")