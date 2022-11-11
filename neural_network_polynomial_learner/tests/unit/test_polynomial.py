import pytest
import sys
sys.path.append("../../")
from polynomial import Polynomial

def test_polynomial():
    poly = Polynomial([2, 3, 0, 5])

    x = 2.0

    derivatives = []

    derivatives.append( 2*x**3 + 3*x**2 + 5) # 0-th derivative
    derivatives.append( 6*x**2 + 6*x       ) # 1-st derivative
    derivatives.append(12*x    + 6         ) # 2-nd derivative
    derivatives.append(12                  ) # 3-rd derivative
    derivatives.append(0                   ) # 4-th derivative

    for i, d in enumerate(derivatives):
        assert(pytest.approx(poly.f(x,i)) == d)