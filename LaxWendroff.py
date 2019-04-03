from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as axes


starting_x = -10
c = 3
length = 20
delta_x = .1
delta_t = .01
sigma = c*delta_t/delta_x
n = int(length/delta_x)

alpha = 0
beta = 0

time = 100

def main():
	A = np.zeros((n-1, n-1))

	for i in range(n-1):
		A[i,i] = -1*(sigma**2 - 1)

	for i in range(n-2):
		A[i,i+1] = .5*sigma*(sigma-1)
		A[i+1,i] = .5*sigma*(sigma+1)

	print(A)

	xvals = np.zeros(n-1)

	for i in range(n-1):
		xvals[i] = starting_x + (i+1)*delta_x
	print("Xvals")
	print(xvals)

	u0 = np.zeros(n-1)

	for i in range(n-1):
		u0[i] = initialConditions(xvals[i])

	print(u0)

	b = np.zeros(n-1)

	b[0] = .5*sigma*(sigma+1)*alpha
	b[n-2] = .5*sigma*(sigma-1)*beta

	print(b)

	ut = u0

	t = time
	while(t > 0):
		ut = np.add(np.matmul(A, np.transpose(ut)), np.transpose(b))
		t = t - 1

	plotGraph(ut, xvals)

def plotGraph(u, xvals):
	y = np.zeros(n+1)
	y[0] = alpha
	y[n] = beta

	x = np.zeros(n+1)
	x[0] = starting_x
	x[n] = starting_x + length

	for i in range(n-1):
		x[i+1] = xvals[i]
		y[i+1] = u[i]

	print(x)
	print(y)

	plt.xlim(starting_x, starting_x+length)
	plt.ylim(0,1)
	plt.plot(x, y)
	plt.plot(x, np.zeros(n+1))

	plt.show()


def initialConditions(x):
	return 1/(1+x**2)

#def printSolution(xvals, ut):

if __name__ == "__main__":
	main()

