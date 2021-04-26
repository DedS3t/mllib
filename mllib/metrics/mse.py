import numpy as np 


def mse(y, y_hat) -> int:
    """Calculate Mean Squared Error (1/n∑(y_i-ŷ_i)^2)
    
    Parameters
    -----------
        y - The actual values
        y_hat - Your predictions

    """
    return (1 / len(y) * sum((y - y_hat) ** 2))

def mse_back_propogate(X, betas, y):
    """Calculates gradient of mse (-2/m * (y - y_hat) dot X)

    Parameters
    -----------
        X - the features
        betas - the betas aka; thetas, params
        y - the targets
    """
    return -2 / len(X) * (y - (X * betas)).dot(X)
    # Good resource for lin reg
    # https://www.ics.uci.edu/~xhx/courses/CS273P/04-linear-regression-273p.pdf
    

    