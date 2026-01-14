import matplotlib.pyplot as plt

def plot_convergence(errors, h_values):
    for method, err in errors.items():
        plt.loglog(h_values, err, marker='o', label=method)

    plt.xlabel("Step size (h)")
    plt.ylabel("Global Error")
    plt.title("Convergence of Runge-Kutta Methods")
    plt.legend()
    plt.grid(True)
    plt.show()
