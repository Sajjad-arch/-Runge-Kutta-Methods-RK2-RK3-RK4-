📊 C2_RungeKutta Project Structure
A comprehensive implementation of Runge-Kutta numerical methods with error analysis and visualization tools.

📁 Project Directory Tree
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
├── ⚙️ solver.py            # ← **Main solver interface**
├── 🚀 main.py              # ← **Entry point**
│
├── 💾 data/
│   └── errors.csv          # Error analysis results
│
├── 🖼️ figures/
│   ├── convergence_plot.png      # Convergence visualization
│   ├── solution_comparison.png   # Solution plots
│   └── accuracy_comparison.png   # Accuracy analysis
│
├── 📖 README.md            # Project documentation
└── 📦 requirements.txt     # Python dependencies
🎯 Key Components
Core Solvers
RK2: Second-order Runge-Kutta (Heun's method)
RK3: Third-order Runge-Kutta
RK4: Fourth-order classical Runge-Kutta
Analysis Tools
Global & local error computation
Convergence rate analysis
Comprehensive visualization suite
Testing & Validation
Unit tests for numerical accuracy
Error validation against analytical solutions
🚀 Quick Start
bash
# Install dependencies
pip install -r requirements.txt

# Run the main program
python main.py
📊 Output
The project generates:

CSV data with error metrics
PNG figures comparing solver accuracy and convergence
Console output with numerical results
Built for numerical analysis and ODE solving

