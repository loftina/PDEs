from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class OneDimensionalHeat:

	def __init__(self, gamma, length, delta_x, delta_t, n, initialConditions, alpha, beta):
		self.gamma = gamma
		self.length = length
		self.delta_x = delta_x
		self.delta_t = delta_t
		self.mu = (gamma*delta_t)/delta_x**2
		self.n = n
		self.alpha = alpha
		self.beta = beta
		self.initialConditions = initialConditions
		makeMatrices(mu, delta_x, initialConditions, alpha, beta)

	def makeMatrices(mu, delta_x, initialConditions, alpha, beta):
		A = np.zeros((n-1, n-1))

		for i in range(n-1):
			A[i,i] = 1-2*mu

		for i in range(n-2):
			A[i,i+1] = mu
			A[i+1,i] = mu

		xvals = np.zeros(n-1)

		for i in range(n-1):
			xvals[i] = (i+1)*delta_x

		u0 = np.zeros(n-1)

		for i in range(n-1):
			u0[i] = initialConditions((i+1)*delta_x)


		b = np.zeros(n-1)

		b[0] = mu*alpha
		b[n-2] = mu*beta

		self.A = A
		self.xvals = xvals
		self.u0 = u0
		self.b = b



	def pprint(self):
		print self.gamma;

def initialConditions(x):
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

def alpha(x):
	return 0

def beta(x):
	return 0

def main():
	test = OneDimensionalHeat(1, 1, .1, .01, 1, 1, 0)
	test.pprint()
	print('hi')

if __name__ == "__main__":
	main()