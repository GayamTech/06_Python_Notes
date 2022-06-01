#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

h = 2**-7
N = int(1/h)


t = np.linspace(0, 1, N+1)

# This is the Exact solution:
x_exact = t * np.arcsin(t)

# function to Compute dx/dt:
def dx_dt(t, x):
    return x/t + t / np.cos(x/t)

# 0. Euler Method:
x_euler = np.zeros(N+1)
for i in range(1, N+1):
    x_euler[i] = x_euler[i-1] + h * dx_dt(float(i)*h, x_euler[i-1])

# 1. Modified Euler Method:
x_mod_euler = np.zeros(N+1)
for i in range(1, N+1):
    dx_dt_1 = dx_dt(float(i)*h, x_mod_euler[i-1])
    dx_dt_2 = dx_dt(float(i)*h, x_euler[i])
    x_mod_euler[i] = x_mod_euler[i-1] + h/2 * (dx_dt_1 + dx_dt_2)

# 2. 4th order RK Method:
x_RK = np.zeros(N+1)
for i in range(1, N+1):
    ti = float(i)*h
    k1 = h * dx_dt(ti, x_RK[i - 1])
    k2 = h * dx_dt(ti + h/2, x_RK[i - 1] + k1/2)
    k3 = h * dx_dt(ti + h/2, x_RK[i - 1] + k2/2)
    k4 = h * dx_dt(ti + h, x_RK[i - 1] + k3)
    x_RK[i] = x_RK[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
# 3. Relative Errors:
    err_euler      = (np.abs((x_euler[1:]      - x_exact[1:]) / x_exact[1:])),
    err_mod_euler   = (np.abs((x_mod_euler[1:]  - x_exact[1:]) / x_exact[1:])),
    err_RK = (np.abs((x_RK[1:]- x_exact[1:]) / x_exact[1:])),



# Plot everything together
plt.plot(t, x_exact, label="Exact")
plt.plot(t, x_euler, label="Euler")
plt.plot(t, x_mod_euler, label="Mod Euler")
plt.plot(t, x_RK, label="RK")
plt.legend()
plt.show()

