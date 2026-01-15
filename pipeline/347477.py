import matplotlib.pyplot as plt
import numpy as np


def plot_function():
	x = np.linspace(-1, 1, 100)	# tutaj uzupełnij
	y = 1/(1+25*(x**2))							# tutaj uzupełnij
	plt.figure()
	plt.plot(x, y)
	plt.savefig("../figures/347477.png")
	return "Figure was succesfully saved"


if __name__=="__main__":
	print(plot_function())
