import matplotlib.pyplot as plt
import numpy as np


def plot_function():
	x = np.linspace(-1, 1, 100)	# tutaj uzupełnij
	y = np.sin(x)							# tutaj uzupełnij
	plt.figure()
	plt.plot(x, y)
	plt.savefig("../figures/twoj_numer_indeksu.png")
	return "Figure was succesfully saved"


if __name__=="__main__":
	print(plot_function())
