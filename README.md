
# Runge-Kutta Methods: Comparative Analysis (C2 Assignment)

## 📋 Project Overview
This project implements and compares three explicit Runge-Kutta methods (RK2, RK3, and RK4) for solving ordinary differential equations (ODEs). It was developed as part of the CSE261 Numerical Methods course at Southeast University, Bangladesh.

**Topic:** C2 - Runge-Kutta Methods (RK2, RK3, RK4)

## 🎯 Objectives
- Implement RK2, RK3, and RK4 algorithms from scratch
- Compare convergence behavior and accuracy
- Validate theoretical order of accuracy through numerical experiments
- Analyze computational efficiency trade-offs

## 🏗️ Project Structure
```
C2_RungeKutta/
│
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
│
├── src/                                # Source code
│   ├── main.py                         # Main driver script
│   ├── solver.py                       # General ODE solver
│   ├── problems/
│   │   └── test_problem.py             # Test ODE definition
│   ├── solvers/
│   │   ├── rk2.py                      # RK2 implementation
│   │   ├── rk3.py                      # RK3 implementation
│   │   └── rk4.py                      # RK4 implementation
│   ├── error_analysis/
│   │   ├── global_error.py             # Error computation
│   │   └── convergence_rate.py         # Convergence rate calculation
│   ├── visualization/
│   │   ├── convergence_plot.py         # Convergence plot generation
│   │   └── solution_plot.py            # Solution comparison plot
│   └── validation/
│       └── unit_tests.py               # Basic validation tests
│
├── data/                               # Generated data files
│   ├── errors.csv                      # Error table data
│   └── convergence_rates.csv           # Convergence rate data
│
├── figures/                            # Generated plots
│   ├── convergence_plot.png            # Convergence analysis plot
│   └── solution_comparison.png         # Solution comparison plot
│
├── report/                             # LaTeX report
│   ├── main.tex                        # Main LaTeX document
│   ├── references.bib                  # Bibliography
│   ├── SEULogo.png                     # University logo
│   └── figures/                        # Report figures
│
└── presentation/                       # Presentation materials
    └── slides.pptx                     # Presentation slides (optional)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/C2_RungeKutta.git
   cd C2_RungeKutta
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Required Python Packages
- `numpy>=1.21.0` - Numerical computations
- `matplotlib>=3.5.0` - Plotting and visualization
- `pandas>=1.3.0` - Data handling (optional)

## 💻 Usage

### Running the Analysis
Execute the main script:
```bash
python src/main.py
```

This will:
1. Solve the test ODE using RK2, RK3, and RK4 methods
2. Generate convergence plots
3. Compute empirical convergence rates
4. Save results to `data/` and `figures/` directories

### Test Problem
The test ODE is:
\[
\frac{dy}{dx} = y, \quad y(0) = 1, \quad x \in [0, 1]
\]
Exact solution: \( y(x) = e^x \)

### Step Sizes Analyzed
The code tests six step sizes: `[0.5, 0.2, 0.1, 0.05, 0.025, 0.01]`

## 📊 Key Results

### Expected Convergence Rates
- **RK2**: \( O(h^2) \) - Error reduces by factor of 4 when h is halved
- **RK3**: \( O(h^3) \) - Error reduces by factor of 8 when h is halved  
- **RK4**: \( O(h^4) \) - Error reduces by factor of 16 when h is halved

### Generated Outputs
1. **Global Error Table** - Errors at final point for each method and step size
2. **Convergence Plot** - Log-log plot showing error vs step size
3. **Solution Comparison Plot** - Numerical vs exact solutions for h=0.2
4. **Empirical Convergence Rates** - Computed from error data

## 🔬 Implementation Details

### Runge-Kutta Methods

#### RK2 (Midpoint Method)
```python
k1 = f(x, y)
k2 = f(x + h/2, y + h/2 * k1)
y_new = y + h * k2
```

#### RK3 (Third-Order Method)
```python
k1 = f(x, y)
k2 = f(x + h/2, y + h/2 * k1)
k3 = f(x + h, y - h*k1 + 2*h*k2)
y_new = y + h/6 * (k1 + 4*k2 + k3)
```

#### RK4 (Classical Fourth-Order)
```python
k1 = f(x, y)
k2 = f(x + h/2, y + h/2 * k1)
k3 = f(x + h/2, y + h/2 * k2)
k4 = f(x + h, y + h * k3)
y_new = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
```

## 📈 Analysis Methods

### Global Error Calculation
\[
E(h) = |y_{\text{num}}(1) - e|
\]

### Empirical Convergence Rate
\[
p_{\text{emp}} \approx \frac{\log(E(h_2)/E(h_1))}{\log(h_2/h_1)}
\]

## 📝 Report & Documentation

### LaTeX Report
The complete report is in the `report/` directory. To compile:
```bash
cd report
pdflatex main.tex
```

### Report Contents
1. Introduction
2. Theoretical Background
3. Numerical Methodology
4. Results and Analysis
5. Conclusion
6. References
7. Appendix (Local error analysis)

## 🧪 Testing
Run basic validation tests:
```bash
python src/validation/unit_tests.py
```

Conclusion
Higher order → higher accuracy
Experimental rates match theory
RK4 best accuracy-efficiency tradeoff


## 🏫 Course Information
- **Course:** CSE261 - Numerical Methods
- **Instructor:** Tashreef Muhammad
- **Institution:** Southeast University, Bangladesh
- **Semester:** Fall 2025

## 📚 References
1. Burden, R. L., & Faires, J. D. (2011). *Numerical Analysis* (9th ed.)
2. Butcher, J. C. (2016). *Numerical Methods for Ordinary Differential Equations* (3rd ed.)
3. Press, W. H., et al. (2007). *Numerical Recipes: The Art of Scientific Computing* (3rd ed.)

## 📄 License
This project is developed for academic purposes as part of the CSE261 course at Southeast University, Bangladesh.

## 🤝 Contributing
This is a course project. External contributions are not accepted.




---

**Last Updated:** December 2025  
**Version:** 1.0
