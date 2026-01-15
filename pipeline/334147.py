import matplotlib.pyplot as plt
import numpy as np


def plot_function():
    x = np.linspace(-np.pi, np.pi, 100)  # tutaj uzupełnij
    y = np.sin(x) + np.cos(2 * x)  # tutaj uzupełnij
    plt.figure()
    plt.plot(x, y)
    plt.savefig("../figures/334147.png")
    return "Figure was succesfully saved"


if __name__ == "__main__":
    print(plot_function())
