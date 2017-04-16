import numpy as np

# finding the zero of a function 

from scipy.optimize import fsolve
f = lambda x: 0.5 - np.exp(-x))  
xzero = fsolve(f,1)
print('result of fsolve:', xzero) 


# CDF of a normal distribution

from scipy.special import erf

def StandardNormalCdf(x):
    return((erf(x / root2) + 1) / 2)

def NormalCdf(x, mu=0, sigma=1):
    return(StandardNormalCdf(float(x - mu) / sigma))
    
    
# Box whisker Plot

import matplotlib.pyplot as plt
import numpy.random as rnd
rnd.seed(10)
data = 2 * rnd.standard_normal(500) + 10.0 
a = plt.boxplot(data)
plt.show()
