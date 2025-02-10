import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. First equation: x'(t) = 1 + t^2 * x(t)^2
def eq1(x, t):
    return 1 + t**2 * x**2

t1 = np.linspace(0, 40, 1000)
initial_conditions1 = [-2, -1, -0.5, 0, 0.5, 1, 2]  # multiple initial conditions
plt.figure(figsize=(15, 10))

# Plot first equation with multiple initial conditions
plt.subplot(2, 2, 1)
for x0 in initial_conditions1:
    sol1 = odeint(eq1, x0, t1)
    plt.plot(t1, sol1)
plt.title("Solution to x'(t) = 1 + t²x(t)²")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.ylim(-3, 3)  # limit y axis to match target

# 2. Second equation system: dx/dt = y, dy/dt = y/2 - x - y^3
def eq2(state, t):
    x, y = state
    dx = y
    dy = y/2 - x - y**3
    return [dx, dy]

t2 = np.linspace(0, 40, 1000)
# More initial conditions in a spiral pattern
r = np.linspace(0.1, 2, 15)
theta = np.linspace(0, 4*np.pi, 15)
initial_conditions = []
for i in range(len(r)):
    initial_conditions.append([r[i]*np.cos(theta[i]), r[i]*np.sin(theta[i])])

# Plot second equation (phase plane)
plt.subplot(2, 2, 2)
for ic in initial_conditions:
    sol = odeint(eq2, ic, t2)
    plt.plot(sol[:, 0], sol[:, 1])
plt.title('Phase Plane for System 2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis([-4, 4, -3, 3])

# 3. Third equation: t^2*x''(t) + tx'(t) + (t^2 - α^2)x(t) = 0, α = 0.5
def eq3_system(state, t):
    x, y = state  # y = x'
    if t == 0:
        t = 1e-10  # avoid division by zero
    alpha = 0.5
    dxdt = y
    dydt = -(1/t)*y - ((t**2 - alpha**2)/(t**2))*x
    return [dxdt, dydt]

t3 = np.linspace(0.1, 40, 1000)

# Plot third equation with more initial conditions
plt.subplot(2, 2, 3)
initial_conditions3 = [
    [1.5, 0], [1, 0], [0.5, 0], 
    [0, 1.5], [0, 1], [0, 0.5],
    [-0.5, 0], [-1, 0], [-1.5, 0],
    [0, -0.5], [0, -1], [0, -1.5]
]
for ic in initial_conditions3:
    sol3 = odeint(eq3_system, ic, t3)
    plt.plot(t3, sol3[:, 0])
plt.title("Solution to t²x''(t) + tx'(t) + (t² - α²)x(t) = 0")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.ylim(-2, 2)  # limit y axis to match target

plt.tight_layout()
plt.show()