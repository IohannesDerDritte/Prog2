#!/usr/bin/env python3.9

from person import Person
from time import perf_counter as pc
from numba import njit
import matplotlib.pyplot as plt
def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)

def main():
	n = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
	timeCPP = []
	timeNJIT = []
	timePy = []
	for x in n:
		f = Person(x)
		start = pc()
		f.fib()
		end = pc()
		timeCPP += [(end - start)]
		print(1)
		start = pc()
		r = fib_numba(x)
		end = pc()
		timeNJIT += [(end - start)]
		print(2)
		start = pc()
		c = fib_py(x)
		end = pc()
		timePy += [(end-start)]
		print(3)
		print(str(x) + ' is done')

	nn = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
	timeNJIT2 = []
	timePy2 = []
	for x in nn:
		start = pc()
		r = fib_numba(x)
		end = pc()
		timeNJIT2 += [(end- start)]

		start = pc()
		c = fib_py(x)
		end = pc()
		timePy2 += [(end-start)]

	f = Person(47)
	print(f.fib())

	t = fib_numba(47)
	print(t)

	plt.figure(1)
	plt.plot(n, timeCPP, color='red')
	plt.plot(n, timeNJIT, color='blue')
	plt.plot(n, timePy, color='green')
	plt.xlabel('n')
	plt.ylabel('time (s)')
	plt.title('Red=Cpp, Blue=Numba, Green=Py')
	plt.savefig('Fig1.png')

	plt.figure(2)
	plt.plot(nn, timeNJIT2, color='blue')
	plt.plot(nn, timePy2, color='green')
	plt.xlabel('n')
	plt.ylabel('time (s)')
	plt.title('Blue=Numba, Green=Py')
	plt.savefig('Fig2.png')

if __name__ == '__main__':
	main()
