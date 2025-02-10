import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation
def dx_dt(x, t):
    return 1 + t**2 * x**2

# Define the time range
t = np.linspace(0, 10, 100)

# Initial condition
x0 = 0

# Solve the differential equation
x = odeint(dx_dt, x0, t)

# Plot the solution
plt.plot(t, x)
plt.title("Solution of x'(t) = 1 + t^2 * x(t)^2")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.show()


def system(vars, t):
    x, y = vars
    dx_dt = y
    dy_dt = y / 2 - x - y**3
    return [dx_dt, dy_dt]

# Initial conditions
initial_conditions = [1, 0]

# Solve the system of differential equations
sol = odeint(system, initial_conditions, t)

# Plot the solutions
plt.plot(t, sol[:, 0], label='x(t)')
plt.plot(t, sol[:, 1], label='y(t)')
plt.title("Solutions of the System of Differential Equations")
plt.xlabel('t')
plt.ylabel('Solutions')
plt.legend()
plt.grid(True)
plt.show()


alpha = 0.5

def system_2nd_order(vars, t):
    x, x_prime = vars
    x_double_prime = -(t * x_prime + (t**2 - alpha**2) * x) / t**2
    return [x_prime, x_double_prime]

# Initial conditions
initial_conditions_2 = [1, 0]  # x(0) = 1, x'(0) = 0

# Solve the system
sol_2 = odeint(system_2nd_order, initial_conditions_2, t)

# Plot the solution
plt.plot(t, sol_2[:, 0], label='x(t)')
plt.title("Solution of the Second-Order Differential Equation")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()
