from typing import List
from copy import deepcopy
from function import Function


class Polynomial(Function):
    """  A class for simply 1-D polynomial functions

    Attributes
    ----------
    coefficients : List[float]
        The polynomial coefficients listed from highest order term coefficients to lowest.
        (Example: 2x^3 + x + 5  would be specified using the list [2, 0, 1, 5])
    """

    @property
    def coefficients(self) -> List[float]:
        return self._coefficients

    @coefficients.setter
    def coefficients(self, coefficients: List[float]):
        self._coefficients = coefficients

    def __init__(self, coefficients: List[float]) -> None:
        self.coefficients = coefficients

    def f(self, x: float, derivative: int=0) -> float:
        y = super().f(x)
        for i, coefficient in zip(range(len(self.coefficients)-1, -1 , -1), self.coefficients):
            if(i - derivative >= 0):
                a = deepcopy(coefficient)
                for d in range(derivative):
                    a = a * (i-d)
                y = y + a * x**(i - derivative)
        return y