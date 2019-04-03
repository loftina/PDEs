
# u'(x) = (u(x+h) - u(x)) / h + O(h)
def finiteDifference(f, x, hs):
	for h in hs:
		uprime = apply(f, x, h)
		print(uprime)
	print('----')

if __name__ == "__main__":
	main()

def main():
	hs = (.1, .01, .001, .0001)
	x = 10
	print()
	finiteDifference(lambda x : x^3, 10, )