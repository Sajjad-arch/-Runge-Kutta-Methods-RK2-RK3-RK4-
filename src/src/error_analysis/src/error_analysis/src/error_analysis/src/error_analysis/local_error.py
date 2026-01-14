Author: Fardous Rahman
Role: Local truncation error analysis
Description: One-step local error comparison of RK methods
"""

from solvers.rk2 import rk2_step
from solvers.rk3 import rk3_step
from solvers.rk4 import rk4_step

def local_error_analysis(f, exact_solution, h=0.1):
    x0 = 0
    y0 = exact_solution(x0)
    exact_next = exact_solution(x0 + h)

    rk2_val = rk2_step(f, x0, y0, h)
    rk3_val = rk3_step(f, x0, y0, h)
    rk4_val = rk4_step(f, x0, y0, h)

    return {
        "RK2": abs(rk2_val - exact_next),
        "RK3": abs(rk3_val - exact_next),
        "RK4": abs(rk4_val - exact_next)
    }
