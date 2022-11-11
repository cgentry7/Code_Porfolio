from abc import ABC

class Function(ABC):
    """ An abstract class for defining functions with derivatives
    """

    def f(self, x: float, derivative: int=0) -> float:
        """ The primary evaluation method for a function

        Parameters
        ----------
        x : float
            The point in the domain at which to evaluate the function
            
        derivative : int
            The derivative order to be evaluated.  This value must be a positive integer (default: 0)

        Returns
        -------
        float
            The function derivative value at point x
        """
        assert(derivative >= 0)
        return 0.0