import numpy as np
from scipy import integrate

# Define the functions for the integrals
def integrand_1(t):
    return np.sqrt(1 - t**2)

def integrand_2(t):
    return np.sqrt(1 - t**2)

# Compute the integrals
I, _ = integrate.quad(integrand_1, 0, 1)
J, _ = integrate.quad(integrand_2, 0, 1/2)

# Estimate π
pi_1 = 4 * I
pi_2 = 12 * (J - np.sqrt(3)/8)

print(f"Estimate of π using I: {pi_1}")
print(f"Estimate of π using J: {pi_2}")
