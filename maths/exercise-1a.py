import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define the symbolic variable
x = sp.symbols('x')

# Define the function f(x) as the summation
f = sum(sp.sin(k**2 * x) / k**5 for k in range(1, 101))

# Print the symbolic representation of the function
sp.pprint(f)

# Convert the symbolic function to a numerical function for plotting
f_lambdified = sp.lambdify(x, f, 'numpy')

# Define the range for x values
x_vals = np.linspace(-10, 10, 400)

# Compute the corresponding y values
y_vals = f_lambdified(x_vals)

# Plot the function f(x)
plt.plot(x_vals, y_vals)
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
