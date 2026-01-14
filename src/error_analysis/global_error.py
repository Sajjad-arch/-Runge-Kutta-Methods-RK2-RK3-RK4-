Author: Member 8
Role: Global error computation
"""

from solver import solve_ode

def compute_global_error(method, f, exact_solution, x_range, y0, h_values):
    errors = []

    for h in h_values:
        x, y = solve_ode(method, f, x_range, y0, h)
        exact = exact_solution(x[-1])
        errors.append(abs(y[-1] - exact))

    return errors
