import matplotlib.pyplot as plt
import numpy as np


def plot_function():
	x = np.linspace(-2, 2, 400)	# tutaj uzupełnij
	y = np.linspace(-2, 2, 400)
	X, Y = meshgrid(x, y)

	F = X**2 + (Y - np.abs(X)**(2/3))**2
	
	plt.figure(figsize=(6,6))
	plt.contour(X, Y, F, levels=[1])
	plt.axis('equal')

	plt.savefig("../figures/323172.png", dpi=300)
	return "Figure was succesfully saved"


if __name__=="__main__":
	print(plot_function())


