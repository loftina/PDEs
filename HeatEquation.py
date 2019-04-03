from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as axes

gamma = 3
length = 2
delta_x = .2
delta_t = delta_x**2/10
mu = (gamma*delta_t)/delta_x**2
n = int(length/delta_x)

alpha = 0
beta = 0

time = 2

def main():
	A = np.zeros((n-1, n-1))

	for i in range(n-1):
		A[i,i] = 1-2*mu

	for i in range(n-2):
		A[i,i+1] = mu
		A[i+1,i] = mu

	print(A)

	xvals = np.zeros(n-1)

	for i in range(n-1):
		xvals[i] = (i+1)*delta_x

	print(xvals)

	u0 = np.zeros(n-1)

	for i in range(n-1):
		u0[i] = initialConditions((i+1)*delta_x)

	print(u0)

	b = np.zeros(n-1)

	b[0] = mu*alpha
	b[n-2] = mu*beta

	print(b)

	ut = u0

	t = time
	while(t > 0):
		ut = np.add(np.matmul(A, np.transpose(ut)), np.transpose(b))
		t = t - 1


	#u1 = np.add(np.matmul(A, np.transpose(u0)), np.transpose(b))

	#print(u1)

	#u2 = np.add(np.matmul(A, np.transpose(u1)), np.transpose(b))

	#print(u2)

	#plt.plot(xvals, u2)
	#plt.show()

	plotGraph(ut, xvals)

def plotGraph(u, xvals):
	y = np.zeros(n+1)
	y[0] = alpha
	y[n] = beta

	x = np.zeros(n+1)
	x[0] = 0
	x[n] = length

	for i in range(n-1):
		x[i+1] = xvals[i]
		y[i+1] = u[i]

	print(x)
	print(y)


	plt.plot(x, y)
	plt.plot(x, np.zeros(n+1))

	plt.show()


def initialConditions2(x):
	if x < 0:
		return null
	elif x < 1/5:
		return -x
	elif x < 7/10:
		return x - 2/5
	elif x <= 1:
		return 1-x
	else:
		return null

def initialConditions(x):
	return -x**2+2*x

#def printSolution(xvals, ut):

if __name__ == "__main__":
	main()

