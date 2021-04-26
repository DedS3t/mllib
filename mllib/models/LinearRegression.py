import numpy as  np 
from ..metrics import mse
import sys

class LinearRegression:
    """Multivariate linear regression class
    """
    def  __init__(self, cost = "mse"):
        if cost == "mse":
            self.cost = mse.mse
            self.back_propogate = mse.mse_back_propogate
        else:
            raise NameError
    
    def fit(self, X, y, lr = 0.0001, epochs = 10000, verbose = False):
        """Train the Linear Regression model
        
        Parameters
        -----------
            X - np.array
                features
            y - np.array
                targets
            lr - float 
                specifies the learning rate
            epochs - int 
                # of epochs
            verbose - bool 
                print insights
        """
        try:
            self.betas = np.zeros((len(X[0])))
        except TypeError:
            self.betas = np.zeros((1))
        for i in range(epochs):
            self.betas -= lr * self.back_propogate(X, self.betas, y)
            if verbose and i % (epochs // 100) == 0:
                print(f"The error is {self.cost(y, self.betas * X)} epoch: {i}")
        return self.betas
    
    def predict(self, X) -> int:
        return self.betas * X

    


