"""
Classical Fourth-Order Runge-Kutta Method (RK4)

Contributor: Member 3
Responsibility:
- High-accuracy time integration
- Careful slope staging and averaging

Additional Contributors:
- Member 7: Verification and testing

Method: RK4 (4th order accuracy)
Global truncation error: O(h⁴)
"""

def rk4_step(f, x, y, h):
    """
    Perform one RK4 step.

    RK4 achieves fourth-order global accuracy by evaluating
    the derivative at four strategically chosen points.

    Parameters
    ----------
    f : callable
        ODE function dy/dx = f(x, y)
    x : float
        Current independent variable
    y : float
        Current dependent variable
    h : float
        Step size

    Returns
    -------
    float
        Approximate solution at x + h
    """

    # Stage 1: slope at start
    k1 = f(x, y)

    # Stage 2: slope at first midpoint
    x_half = x + 0.5 * h
    y_half_1 = y + 0.5 * h * k1
    k2 = f(x_half, y_half_1)

    # Stage 3: refined midpoint slope
    y_half_2 = y + 0.5 * h * k2
    k3 = f(x_half, y_half_2)

    # Stage 4: slope at endpoint
    x_end = x + h
    y_end = y + h * k3
    k4 = f(x_end, y_end)

    # Weighted average of all slopes
    y_next = y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return y_next


def solve_rk4(f, x0, y0, x_end, h):
    """
    Solve IVP using RK4 from x0 to x_end with step size h.
    
    Parameters
    ----------
    f : callable
        ODE function f(x, y)
    x0 : float
        Initial x value
    y0 : float
        Initial y value at x0
    x_end : float
        Final x value
    h : float
        Step size
    
    Returns
    -------
    x_values : numpy.ndarray
        Array of x values
    y_values : numpy.ndarray
        Array of corresponding y values
    """
    import numpy as np
    
    # Calculate number of steps
    n_steps = int(np.ceil((x_end - x0) / h)) + 1
    
    # Initialize arrays
    x_values = np.zeros(n_steps)
    y_values = np.zeros(n_steps)
    
    # Set initial conditions
    x_values[0] = x0
    y_values[0] = y0
    
    # Perform RK4 steps
    for i in range(n_steps - 1):
        y_values[i+1] = rk4_step(f, x_values[i], y_values[i], h)
        x_values[i+1] = x_values[i] + h
    
    return x_values, y_values


# Quick test if file is run directly
if __name__ == "__main__":
    # Test function: dy/dx = y
    def test_function(x, y):
        return y
    
    print("Testing RK4 implementation...")
    print("-" * 40)
    
    # Test 1: Single step
    result = rk4_step(test_function, 0.0, 1.0, 0.1)
    expected = 1.1051708333333333
    error_step = abs(result - expected)
    
    print(f"Single step test (h=0.1):")
    print(f"  Computed:  {result:.12f}")
    print(f"  Expected:  {expected:.12f}")
    print(f"  Error:     {error_step:.2e}")
    
    if error_step < 1e-10:
        print("  ✅ Single step PASSED")
    else:
        print("  ❌ Single step FAILED")
    
    # Test 2: Full solution
    x_vals, y_vals = solve_rk4(test_function, 0.0, 1.0, 1.0, 0.1)
    import math
    y_exact = math.exp(1.0)
    error_full = abs(y_vals[-1] - y_exact)
    
    print(f"\nFull solution test (x=1, h=0.1):")
    print(f"  RK4 result: {y_vals[-1]:.12f}")
    print(f"  Exact:      {y_exact:.12f}")
    print(f"  Error:      {error_full:.2e}")
    
    if error_full < 1e-6:
        print("  ✅ Full solution PASSED")
    else:
        print("  ❌ Full solution FAILED")
    
    print("-" * 40)
    if error_step < 1e-10 and error_full < 1e-6:
        print("✅ RK4 implementation is CORRECT")
    else:
        print("❌ RK4 implementation needs FIXING")