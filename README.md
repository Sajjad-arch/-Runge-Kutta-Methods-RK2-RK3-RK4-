# 🧮 Runge-Kutta Numerical Methods

A comprehensive Python implementation of Runge-Kutta methods (RK2, RK3, RK4) for solving ordinary differential equations (ODEs) with complete error analysis and visualization tools.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Methods Implemented](#methods-implemented)
- [Examples](#examples)
- [Error Analysis](#error-analysis)
- [Visualization](#visualization)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project provides a modular and extensible framework for solving ordinary differential equations using various Runge-Kutta methods. It includes comprehensive error analysis, convergence studies, and visualization tools to compare the accuracy and efficiency of different numerical methods.

### Key Capabilities

- ✅ Multiple Runge-Kutta solvers (2nd, 3rd, and 4th order)
- 📊 Global and local error analysis
- 📈 Convergence rate computation
- 🎨 Rich visualization suite
- ✔️ Comprehensive unit tests
- 📁 CSV data export for further analysis

---

## ✨ Features

- **Multiple Solver Orders**: RK2, RK3, and RK4 implementations
- **Error Analysis**: Compute global and local truncation errors
- **Convergence Studies**: Analyze convergence rates as step size decreases
- **Visualization**: Generate publication-quality plots
- **Modular Design**: Easy to extend with new methods
- **Well-Tested**: Comprehensive unit test suite
- **Data Export**: Save results to CSV for external analysis

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/C2_RungeKutta.git
cd C2_RungeKutta
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Dependencies

```
numpy>=1.19.0
matplotlib>=3.3.0
scipy>=1.5.0
pandas>=1.1.0
pytest>=6.0.0
```

---

## 📁 Project Structure

```
C2_RungeKutta/
│
├── 🔧 solvers/
│   ├── rk2.py              # 2nd-order Runge-Kutta solver
│   ├── rk3.py              # 3rd-order Runge-Kutta solver
│   ├── rk4.py              # 4th-order Runge-Kutta solver
│   └── base_solver.py      # Base class for all solvers
│
├── 📐 problems/
│   └── test_problem.py     # Test differential equations
│
├── 📉 error_analysis/
│   ├── global_error.py     # Global error computation
│   └── convergence_rate.py # Convergence rate analysis
│
├── 📈 visualization/
│   ├── convergence_plot.py    # Convergence visualization
│   ├── solution_plot.py       # Solution comparison plots
│   └── accuracy_plot.py       # Accuracy analysis plots
│
├── ✅ validation/
│   ├── unit_tests.py       # Unit testing suite
│   └── local_error.py      # Local error analysis
│
├── ⚙️ solver.py            # Main solver interface
├── 🚀 main.py              # Entry point
│
├── 💾 data/
│   └── errors.csv          # Error analysis results
│
├── 🖼️ figures/
│   ├── convergence_plot.png      # Convergence visualization
│   ├── solution_comparison.png   # Solution plots
│   └── accuracy_comparison.png   # Accuracy analysis
│
├── 📖 README.md
└── 📦 requirements.txt
```

---

## 💻 Usage

### Quick Start

Run the main program with default settings:

```bash
python main.py
```

### Basic Example

```python
from solvers.rk4 import RK4Solver

# Define the ODE: dy/dt = -2ty
def f(t, y):
    return -2 * t * y

# Initial condition
y0 = 1.0

# Time span and step size
t_span = (0, 2)
h = 0.1

# Create solver and solve
solver = RK4Solver(f, y0, t_span, h)
t, y = solver.solve()

print(f"Solution at t={t[-1]}: y={y[-1][0]:.6f}")
```

### Using Different Solvers

```python
from solvers.rk2 import RK2Solver
from solvers.rk3 import RK3Solver
from solvers.rk4 import RK4Solver

# Compare all three methods
solvers = [
    RK2Solver(f, y0, t_span, h),
    RK3Solver(f, y0, t_span, h),
    RK4Solver(f, y0, t_span, h)
]

for solver in solvers:
    t, y = solver.solve()
    print(f"{solver.name}: Final value = {y[-1][0]:.6f}")
```

---

## 🔬 Methods Implemented

### RK2 (Heun's Method)
Second-order Runge-Kutta method with local truncation error O(h³).

**Formula:**
```
k₁ = f(tₙ, yₙ)
k₂ = f(tₙ + h, yₙ + h·k₁)
yₙ₊₁ = yₙ + (h/2)·(k₁ + k₂)
```

### RK3
Third-order Runge-Kutta method with local truncation error O(h⁴).

**Formula:**
```
k₁ = f(tₙ, yₙ)
k₂ = f(tₙ + h/2, yₙ + (h/2)·k₁)
k₃ = f(tₙ + h, yₙ - h·k₁ + 2h·k₂)
yₙ₊₁ = yₙ + (h/6)·(k₁ + 4k₂ + k₃)
```

### RK4 (Classic)
Fourth-order Runge-Kutta method with local truncation error O(h⁵).

**Formula:**
```
k₁ = f(tₙ, yₙ)
k₂ = f(tₙ + h/2, yₙ + (h/2)·k₁)
k₃ = f(tₙ + h/2, yₙ + (h/2)·k₂)
k₄ = f(tₙ + h, yₙ + h·k₃)
yₙ₊₁ = yₙ + (h/6)·(k₁ + 2k₂ + 2k₃ + k₄)
```

---

## 📊 Error Analysis

### Global Error

Compute the maximum absolute error over the entire solution:

```python
from error_analysis.global_error import compute_global_error

# Assuming you have numerical and analytical solutions
error = compute_global_error(t, y_numerical, y_analytical)
print(f"Global error: {error:.2e}")
```

### Convergence Rate

Analyze how error decreases with step size:

```python
from error_analysis.convergence_rate import convergence_study

step_sizes = [0.1, 0.05, 0.025, 0.0125]
errors, rates = convergence_study(solver_class, f, y0, t_span, step_sizes)

print(f"Convergence rate: {np.mean(rates):.2f}")
```

---

## 📈 Visualization

### Generate All Plots

```bash
python main.py --plot-all
```

### Individual Visualizations

**Solution Comparison:**
```python
from visualization.solution_plot import plot_solutions

plot_solutions(solvers, analytical_solution)
```

**Convergence Plot:**
```python
from visualization.convergence_plot import plot_convergence

plot_convergence(step_sizes, errors_dict)
```

**Accuracy Comparison:**
```python
from visualization.accuracy_plot import plot_accuracy

plot_accuracy(solvers, y_exact)
```

---

## ✅ Testing

Run the complete test suite:

```bash
pytest validation/unit_tests.py -v
```

Run specific tests:

```bash
pytest validation/unit_tests.py::test_rk4_order -v
```

### Test Coverage

- ✔️ Solver accuracy verification
- ✔️ Order of convergence validation
- ✔️ Edge cases and boundary conditions
- ✔️ Error computation correctness

---

## 📚 Examples

### Example 1: Exponential Decay

```python
import numpy as np
from solvers.rk4 import RK4Solver

# dy/dt = -λy, with λ = 1
def f(t, y):
    return -y

y0 = 1.0
t_span = (0, 5)
h = 0.1

solver = RK4Solver(f, y0, t_span, h)
t, y = solver.solve()

# Analytical solution
y_exact = np.exp(-t)

# Compare
import matplotlib.pyplot as plt
plt.plot(t, y[:, 0], 'o-', label='RK4')
plt.plot(t, y_exact, '--', label='Exact')
plt.legend()
plt.show()
```

### Example 2: Oscillator

```python
# d²y/dt² + ω²y = 0, convert to system:
# dy₁/dt = y₂
# dy₂/dt = -ω²y₁

def oscillator(t, y):
    omega = 1.0
    return np.array([y[1], -omega**2 * y[0]])

y0 = [1.0, 0.0]  # Initial position and velocity
t_span = (0, 10)
h = 0.01

solver = RK4Solver(oscillator, y0, t_span, h)
t, y = solver.solve()

# Plot trajectory
plt.plot(y[:, 0], y[:, 1])
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.title('Phase Space')
plt.show()
```

---

## 🔧 Configuration

Edit `main.py` to customize:

- Test problems
- Step sizes for convergence study
- Plot styles and output formats
- Error tolerance levels

---

## 📖 References

1. **Numerical Methods**: 
   - Burden, R. L., & Faires, J. D. (2010). *Numerical Analysis*
   
2. **Runge-Kutta Methods**:
   - Butcher, J. C. (2016). *Numerical Methods for Ordinary Differential Equations*

3. **Error Analysis**:
   - Hairer, E., Nørsett, S. P., & Wanner, G. (1993). *Solving Ordinary Differential Equations I*

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution

- Additional RK methods (RK5, adaptive methods)
- More test problems
- Performance optimizations
- Documentation improvements
- Additional visualization options

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Your Name** - *Initial work*

---

## 🙏 Acknowledgments

- Thanks to the numerical analysis community
- Inspired by classical ODE textbooks
- Built with Python scientific computing stack

---

## 📞 Contact

For questions or suggestions, please open an issue or contact:
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

---

## 🔄 Version History

- **v1.0.0** (2026-01-14)
  - Initial release
  - RK2, RK3, RK4 implementations
  - Complete error analysis suite
  - Visualization tools

---

**⭐ If you find this project useful, please consider giving it a star!**
