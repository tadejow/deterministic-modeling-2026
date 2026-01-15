import matplotlib.pyplot as plt
import numpy as np


def plot_function():
	x = np.linspace(-10, 10, 100)	# tutaj uzupełnij
	y = np.sin(x)*x							# tutaj uzupełnij
	plt.figure()
	plt.plot(x, y)
	plt.savefig("../figures/346112.png")
	return "Figure was succesfully saved"


if __name__=="__main__":
	print(plot_function())
