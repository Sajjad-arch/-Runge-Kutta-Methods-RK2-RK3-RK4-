
============================================================
Runge-Kutta Methods – Complete Single-File Implementation
RK2, RK3, RK4 + Error Analysis + Convergence Plot
============================================================

```python
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Test Problem Definition
# dy/dx = y , y(0) = 1 , exact solution y = exp(x)
# ------------------------------------------------------------

def f(x, y):
    return y

def exact_solution(x):
    return np.exp(x)

# ------------------------------------------------------------
# Runge-Kutta Methods
# ------------------------------------------------------------

def rk2(f, x0, y0, x_end, h):
    x = x0
    y = y0
    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        y += k2
        x += h
    return y

def rk3(f, x0, y0, x_end, h):
    x = x0
    y = y0
    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h, y - k1 + 2 * k2)
        y += (k1 + 4 * k2 + k3) / 6
        x += h
    return y

def rk4(f, x0, y0, x_end, h):
    x = x0
    y = y0
    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y

# ------------------------------------------------------------
# Global Error Calculation
# ------------------------------------------------------------

def global_error(method, h):
    y_num = method(f, 0.0, 1.0, 1.0, h)
    y_exact = exact_solution(1.0)
    return abs(y_num - y_exact)

# ------------------------------------------------------------
# Convergence Rate Calculation
# ------------------------------------------------------------

def convergence_rate(e1, e2, h1, h2):
    return np.log(e1 / e2) / np.log(h1 / h2)

# ------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------

h_values = [0.5, 0.2, 0.1, 0.05]

rk2_errors = []
rk3_errors = []
rk4_errors = []

for h in h_values:
    rk2_errors.append(global_error(rk2, h))
    rk3_errors.append(global_error(rk3, h))
    rk4_errors.append(global_error(rk4, h))

# ------------------------------------------------------------
# Print Error Table
# ------------------------------------------------------------

print("Step Size | RK2 Error | RK3 Error | RK4 Error")
print("---------------------------------------------")
for i in range(len(h_values)):
    print(f"{h_values[i]:<9} | {rk2_errors[i]:.3e} | {rk3_errors[i]:.3e} | {rk4_errors[i]:.3e}")

# ------------------------------------------------------------
# Convergence Rates
# ------------------------------------------------------------

rk2_rate = convergence_rate(rk2_errors[1], rk2_errors[2], h_values[1], h_values[2])
rk3_rate = convergence_rate(rk3_errors[1], rk3_errors[2], h_values[1], h_values[2])
rk4_rate = convergence_rate(rk4_errors[1], rk4_errors[2], h_values[1], h_values[2])

print("\nConvergence Rates")
print("-----------------")
print(f"RK2 ≈ {rk2_rate:.2f}")
print(f"RK3 ≈ {rk3_rate:.2f}")
print(f"RK4 ≈ {rk4_rate:.2f}")

# ------------------------------------------------------------
# Convergence Plot (Log-Log)
# ------------------------------------------------------------

plt.figure()
plt.loglog(h_values, rk2_errors, marker='o', label='RK2')
plt.loglog(h_values, rk3_errors, marker='s', label='RK3')
plt.loglog(h_values, rk4_errors, marker='^', label='RK4')
plt.xlabel("Step Size (h)")
plt.ylabel("Global Error")
plt.title("Runge-Kutta Convergence Comparison")
plt.legend()
plt.grid(True, which="both")
plt.show()



