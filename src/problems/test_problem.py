def f(x, y):
    """Test ODE: dy/dx = y"""
    return y

def exact_solution(x):
    """Exact solution y = e^x"""
    return np.exp(x)
