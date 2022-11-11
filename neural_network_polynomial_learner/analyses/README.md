# Quadratic Neural Network

In this example, we train neural networks (NN) to fit a simple quadratic function.  All NNs use one 64 node
hidden layer with a target training cumulative loss of 1E-2.

The first NN relies entirely on 0-th order derivative data for training.
This serves as an analog to training exclusively with labeled data.  To demonstrate the limits
of its ability to extrapolate, we train only on a small portion of the domain with only 100 training points.
We can observe that the "labeled data only" (i.e. "f_100") model does not extrapolate beyond the training
region, though it predicts well within the training region.

The second NN trains using 1 labeled data training point and 100 1st derivative training points.
Training almost exclusively using the 1-st derivative data serves as our analogue for "informing" the NN
with information other than the labeled data (i.e. 0th order data).  Again, this is intened to illustrate
the principle behind physics informed neural networks.  It should be noted that the 1st derivative data
comes from the entire domain and is not just limited to a small portion like in the "labeled data only"
case.  This is inline with how physics informing would be applied (i.e. over the entire domain). Also,
the single labeled point is needed to act as an achor point.  Without said point, the neural network
might train to the correct function shape, but would have insufficient information to know where to
center it.  As we can see in the results, the NN matches the reference solution almost exactly, providing
evidence that one might be able to augment limited label data training with additional derivative information.

The final NN trains using 1 labeled data training point, 1 1st derivative training point, and
100 2nd derivative training points.  Similar principles as before apply.  In these results we observe
that though it predicts the shape well, the results are a little offset from the reference.  This might
be due to the fact that the second derivative is less informative than the first derivative.

![image](https://user-images.githubusercontent.com/25329687/201429187-ff9b93ea-a86e-4e1a-9d22-c3084819d142.png)
