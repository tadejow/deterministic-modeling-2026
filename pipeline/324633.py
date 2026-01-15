import matplotlib.pyplot as plt
import numpy as np


def plot_function():
	x = np.linspace(-1, 1, 150)	# tutaj uzupełnij
	y = np.cos(x)							# tutaj uzupełnij
	plt.figure()
	plt.plot(x, y)
	plt.savefig("../figures/324633.png")
	return "Figure was succesfully saved"


if __name__=="__main__":
	print(plot_function())
