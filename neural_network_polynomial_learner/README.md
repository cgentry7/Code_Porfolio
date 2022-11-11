# Polynomial Learner

A demonstration of how one can augment neural network training by enforcing constraints beyond just the labeled data loss.  In this case the neural network is being trained to fit some function with known derivatives.  The neural network can then be trained using any number of evaluation points on the base function (i.e. the labeled data) or its derivatives.  This essentially provides an academic example of the base premise behind Physics Informed Neural Networks (PINNs) [1], wherein one need not train entirely using labeled data, but may rather leverage other known relationships to augment training in the event one is training data poor.

Version / Module Requirements
-----------------------------
- Written using Python 3.10.6
- Pytest module required for execution of unit tests

User Instructions
------------------
A demonstration for how to properly use the polynomial and neural_network classes may be found under the `analyses` folder

References
----------

1. Raissi, Maziar, Paris Perdikaris, and George E. Karniadakis. "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations." Journal of Computational Physics 378 (2019): 686-707 (GitHub: https://github.com/maziarraissi/PINNs)