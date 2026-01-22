import matplotlib.pyplot as plt
import numpy as np


def plot_function():
	x = np.linspace(-1, 1, 100)	
	y = 2*np.sin(2*np.sin(x))			
	plt.figure()
	plt.plot(x, y)
	plt.savefig("../figures/345688.png")
	return "Figure was succesfully saved"


if __name__=="__main__":
	print(plot_function())
