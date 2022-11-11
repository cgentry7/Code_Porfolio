import numpy as np
import pylab as plt
import sys
sys.path.append("../")
from polynomial import Polynomial
from derivative_informed_nn import DerivativeInformedNN

full_domain      = [-20.0, 20.0]
full_domain_1    = np.zeros((1,   1), dtype=np.double); full_domain_1[:,0]    = np.linspace(min(full_domain), max(full_domain), 1)
full_domain_100  = np.zeros((100, 1), dtype=np.double); full_domain_100[:,0]  = np.linspace(min(full_domain), max(full_domain), 100)
full_domain_1000 = np.zeros((1000,1), dtype=np.double); full_domain_1000[:,0] = np.linspace(min(full_domain), max(full_domain), 1000)

half_domain      = [0., 10.0]
half_domain_1    = np.zeros((1,   1), dtype=np.double); half_domain_1[:,0]    = np.linspace(min(half_domain), max(half_domain), 1)
half_domain_100  = np.zeros((100, 1), dtype=np.double); half_domain_100[:,0]  = np.linspace(min(half_domain), max(half_domain), 100)
half_domain_1000 = np.zeros((1000,1), dtype=np.double); half_domain_1000[:,0] = np.linspace(min(half_domain), max(half_domain), 1000)

poly        = Polynomial([2, 1, 1])
test_points = full_domain_1000
reference_y = [poly.f(x) for x in test_points[:,0]]

hidden_layers_num_nodes = [64]
dropouts = [1.0]

# Only using "labeled" data to train with
training_points = [half_domain_100] #0-th order derivative
d0_trained_data_nn = DerivativeInformedNN(poly, training_points, full_domain, hidden_layers_num_nodes, dropouts)
d0_trained_data_nn.train(convergence_criteria=1E-2)
d0_trained_data_y = d0_trained_data_nn.F(test_points)

# Using one labeled data point and 100 first order derivative points
training_points = [half_domain_1, full_domain_100] 
d1_trained_data_nn = DerivativeInformedNN(poly, training_points, full_domain, hidden_layers_num_nodes, dropouts)
d1_trained_data_nn.train(convergence_criteria=1E-2)
d1_trained_data_y = d1_trained_data_nn.F(test_points)

# Using one labeled data point and 100 second order derivative points (can't skip first order derivative so have to pass it 1 sized array)
training_points = [half_domain_1, full_domain_1, full_domain_100] 
d2_trained_data_nn = DerivativeInformedNN(poly, training_points, full_domain, hidden_layers_num_nodes, dropouts)
d2_trained_data_nn.train(convergence_criteria=1E-2)
d2_trained_data_y = d2_trained_data_nn.F(test_points)

plt.plot(test_points[:,0],  reference_y,            linestyle=':',  label="ref")
plt.plot(test_points[:,0],  d0_trained_data_y[:,0], linestyle='-',  label="f_100")
plt.plot(test_points[:,0],  d1_trained_data_y[:,0], linestyle='-.', label="f_1_df_100")
plt.plot(test_points[:,0],  d2_trained_data_y[:,0], linestyle='--', label="f_1_df_1_d2f_100")

plt.legend()
plt.show()