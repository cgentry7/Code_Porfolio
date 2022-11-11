import pytest
import numpy as np
import sys
sys.path.append("../../")
from polynomial import Polynomial
from derivative_informed_nn import DerivativeInformedNN

domain      = [-5.0, 5.0]
domain_100  = np.zeros((100, 1), dtype=np.double); domain_100[:,0]  = np.linspace(min(domain), max(domain), 100)
domain_1000 = np.zeros((1000,1), dtype=np.double); domain_1000[:,0] = np.linspace(min(domain), max(domain), 1000)

poly        = Polynomial([4, 3, 1])
test_points = domain_1000
true_Y      = [poly.f(x) for x in test_points[:,0]]

hidden_layers_num_nodes = [16, 8  ]
dropouts                = [1., 1.0]

training_points = [domain_100, domain_100]

# Test Initialization
neutral_net = DerivativeInformedNN(poly, training_points, domain, hidden_layers_num_nodes, dropouts)
assert(neutral_net.function is poly)
assert(neutral_net.training_points is training_points)
assert(neutral_net.bounds is domain)
assert(neutral_net.hidden_layers_num_nodes is hidden_layers_num_nodes)
assert(neutral_net.dropouts is dropouts)

# Test training method
neutral_net.train(epoch_limit=10000, convergence_criteria=1E-1)

# Test prediction method
pred_Y   = neutral_net.F(test_points   )
pred_dY  = neutral_net.F(test_points, 1)