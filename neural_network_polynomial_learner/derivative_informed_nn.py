from typing import List
import time
import numpy as np
import tensorflow.compat.v1 as tf
from tensorflow.keras import layers
from tensorflow.keras import backend as K
from function import Function


class DerivativeInformedNN(object):
    """ This is a neural network class which is meant to learn a given function and can use the function's
        derivatives to help augment training

    Attributes
    ----------
    function : Function
        The function which the neural network will attempt to learn from
    
    training_points : List[np.ndarray]
        The training points which will be used to train the neural network.  Here "points" include both
        the x-position within the domain, as well as which derivative is to be evaluated.  This is a 2-D
        array with the first dimension corresponding to the derivative order and the second dimension the
        collection of x-points to be considered for that derivative. (ex: [[1.0, 3.0], [2.0, 5.0, 7.0]]
        instructs the neural net to train on the 0-th derivative at points 1.0 and 3.0, and on the 1-st
        derivative on points 2.0, 5.0, and 7.0)

    bounds : List[float]
        The upper and lower boundaries on which that the neural network has been trained to.

    hidden_layer_num_nodes : List[int]
        The number of nodes for each hidden layer

    dropouts : List[float]
        The dropout probability to be applied at each hidden layer (must be 0 <= p <= 1.0)
        (default: All layer dropout rates set to 0.0)
    """
    
    @property
    def function(self) -> Function:
        return self._function

    @property
    def training_points(self) -> List[List[float]]:
        return self._training_points

    @property
    def bounds(self) -> List[float]:
        return self._bounds

    @property
    def hidden_layers_num_nodes(self) -> List[int]:
        return self._hidden_layers_num_nodes

    @property
    def dropouts(self) -> List[float]:
        return self._dropouts

    def __init__(self, function:                  Function,
                       training_points:           List[np.ndarray],
                       bounds:                    List[float],
                       hidden_layers_num_nodes:   List[int],
                       dropouts:                  List[float]) -> None:

        assert(all(points.ndim == 2 for points in training_points))
        assert(all(points.shape[1] == 1 for points in training_points))
        assert(len(bounds) == 2)
        assert(all([num_nodes > 0 for num_nodes in hidden_layers_num_nodes]))
        assert(len(hidden_layers_num_nodes) == len(dropouts))
        assert(all([dropout >= 0.0 and dropout <= 1.0 for dropout in dropouts]))

        self._function = function
        self._bounds = bounds
        self._hidden_layers_num_nodes = hidden_layers_num_nodes
        self._dropouts = dropouts
        self._training_points = training_points

        self._init_tensorflow()


    def train(self, epoch_limit: int=100000000, convergence_criteria: float=1E-19) -> None:
        """ The method which initiates training of the neural network

        Parameters
        ----------
        epoch_limit : int
            The maximum number of training epochs to run (default: 100000000)
        convergence_criteria : float
            The termination criteria for the aggregate training loss (default: 1E-19)
        """

        assert(epoch_limit > 0)
        assert(convergence_criteria > 0)

        start_time = time.time()
        epoch = 0
        loss  = 2.0 * convergence_criteria
        while(epoch < epoch_limit and loss > convergence_criteria): 
            self._tf_session.run(self._adam_optimizer, self._tensor_flow_variables)
            epoch += 1
            if epoch % 100 == 0:
                elapsed_time = time.time() - start_time
                loss = self._tf_session.run(self._loss, self._tensor_flow_variables)
                print('Epoch: %d, Loss: %.3e, Time: %.2f' % (epoch, loss, elapsed_time))
                start_time = time.time()


    def F(self, X: np.ndarray, derivative: int=0) -> np.ndarray:
        """ The primary predictor for the model

        Parameters
        ----------
        X : np.ndarray
            The points in the domain at which to evaluate the function
            
        derivative : int
            The derivative order to be evaluated.  This value must be a positive integer (default: 0)

        Returns
        -------
        np.ndarray
            The function derivative values at points X
        """

        Y = self._tf_session.run(self._pred_Y[derivative], {self._X[derivative]: X})
        return Y

    def _init_tensorflow(self) -> None:
        """ A helper method to setup the tensorflow session and associated variables
        """

        # At the time I originally wrote this script, I was using TF around 2019 or 2020, so this way of 
        # using TF is a little out of date.  I'll probably update this stuff later, but for now, I'm just
        # going to use TF V1
        tf.disable_v2_behavior()

        self._init_neural_net()
      
        self._tf_session = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                                                            log_device_placement=True))

        self._tensor_flow_variables = {}

        self._X      = []
        self._true_Y = []
        self._pred_Y = []
        self._loss   = 0.0
        for d in range(len(self.training_points)):
            self._X.append(tf.placeholder(tf.float32, shape=[None,1]))
            self._true_Y.append(tf.placeholder(tf.float32, shape=[None,1]))
            self._pred_Y.append(self._pred_F(self._X[d], d))
            self._loss = self._loss + tf.reduce_mean(tf.square(self._true_Y[d] - self._pred_Y[d]))
            self._tensor_flow_variables[self._X[d]] = self.training_points[d]
            self._tensor_flow_variables[self._true_Y[d]] = np.array([self.function.f(x, d) for x in self.training_points[d]]) 

        self._optimizer = tf.train.AdamOptimizer()
        self._adam_optimizer = self._optimizer.minimize(self._loss)

        tf_initializer = tf.global_variables_initializer()
        self._tf_session.run(tf_initializer)


    def _init_neural_net(self):
        """ A helper method to setup the neural network to be trained   
        """

        num_nodes = [1]                                                    # Add the initial layer (has only one node)
        for nodes in self.hidden_layers_num_nodes: num_nodes.append(nodes) # Add the hidden layers
        num_nodes.append(1)                                                # Add the final layer   (has only one node)

        self._weights = []
        self._biases  = []

        num_layers = len(num_nodes)
        for l in range(num_layers-1):

            #Initialize Weights using Xavier Initialization
            xavier_stddev = np.sqrt(2/(num_nodes[l] + num_nodes[l+1]))
            W = tf.Variable(tf.random.truncated_normal([num_nodes[l], num_nodes[l+1]], stddev=xavier_stddev), dtype=tf.float32)

            #Initialize biases to Zero
            b = tf.Variable(tf.zeros([1,num_nodes[l+1]], dtype=tf.float32), dtype=tf.float32)

            self._weights.append(W)
            self._biases.append(b)

    def _pred_F(self, X: np.ndarray, derivative: int=0) -> np.ndarray:
        """ The tensorflow evaluation method for the model

        Parameters
        ----------
        X : np.ndarray
            The points in the domain at which to evaluate the function
            
        derivative : int
            The derivative order to be evaluated.  This value must be a positive integer (default: 0)

        Returns
        -------
        np.ndarray
            The function derivative values at points X
        """

        assert(derivative >= 0)

        #Normalize the input to 1.0
        H = 2.0*(X - min(self.bounds)) / (max(self.bounds) - min(self.bounds)) - 1.0

        #Predict Y given X
        num_layers = len(self._weights) + 1
        for l in range(0,num_layers-2):
          W = self._weights[l]
          b = self._biases[l]
          H = tf.tanh(tf.add(tf.matmul(H, W), b))
          H = tf.nn.dropout(H, self.dropouts[l]) 
        W = self._weights[-1]
        b = self._biases[-1]
        Y = tf.add(tf.matmul(H, W), b)

        #Perform auto-derivative (for cases where a non-zero order derivative is desired)
        for d in range(derivative):
            Y = tf.gradients(Y,X)
        return Y