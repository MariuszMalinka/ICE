import numpy as np

def estimation(x,y):
    ## b is the array of coefficients standing by the values in the equation determining the optimal output value 
    ## Mathematical notation b = (X^T X)^(-1) X^T Y 
    b=np.matmul(np.matmul(np.linalg.inv(np.matmul(x.T,x)),x.T),y)
    return b