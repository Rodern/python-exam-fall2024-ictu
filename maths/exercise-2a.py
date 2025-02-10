import numpy as np
from scipy import optimize

# Define the equation
def equation(x):
    return np.cos(x) - x

# Find the root of the equation
root = optimize.root_scalar(equation, bracket=[0, 1])
print(f"Root: {root.root}")
