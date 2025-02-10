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

# Compute the first derivative of the function
f_prime = sp.diff(f, x)

# Compute the second derivative of the function
f_double_prime = sp.diff(f_prime, x)

# Print the symbolic representation of the derivatives
sp.pprint(f_prime)
sp.pprint(f_double_prime)

# Convert the derivatives to numerical functions for plotting
f_prime_lambdified = sp.lambdify(x, f_prime, 'numpy')
f_double_prime_lambdified = sp.lambdify(x, f_double_prime, 'numpy')

# Compute the corresponding y values for the derivatives
y_prime_vals = f_prime_lambdified(x_vals)
y_double_prime_vals = f_double_prime_lambdified(x_vals)

# Plot the function f(x)
plt.figure()
plt.plot(x_vals, y_vals)
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Plot the first derivative f'(x)
plt.figure()
plt.plot(x_vals, y_prime_vals)
plt.title("Graph of f'(x)")
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.grid(True)

# Plot the second derivative f''(x)
plt.figure()
plt.plot(x_vals, y_double_prime_vals)
plt.title("Graph of f''(x)")
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.grid(True)

# Show all plots
plt.show()
