import matplotlib.pyplot as plt
import numpy as np
from solver import solve_ode

def plot_solutions(methods, f, exact_solution, x_range, y0, h):
    x_exact = np.linspace(x_range[0], x_range[1], 200)
    y_exact = exact_solution(x_exact)

    plt.plot(x_exact, y_exact, label="Exact", linewidth=2)

    for name, method in methods.items():
        x, y = solve_ode(method, f, x_range, y0, h)
        plt.plot(x, y, '--o', label=name)

    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.title("Numerical vs Exact Solution")
    plt.legend()
    plt.grid(True)
    plt.show()
