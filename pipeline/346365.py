import matplotlib.pyplot as plt
import numpy as np


def plot_function():
	x = np.linspace(-1, 10, 500)	#
	y = np.exp(x) - 4321			#
	plt.figure()
	plt.plot(x, y)
	plt.savefig("../figures/346365.png")
	return "Figure was succesfully saved"


if __name__=="__main__":
	print(plot_function())

