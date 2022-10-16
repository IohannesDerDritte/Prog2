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
	n = [30, 35, 40]
	timeCPP = []
	timeNJIT = []
	timePy = []
	for x in n:
		f = Person(x)
		start = pc()
		f.fib()
		end = pc()
		timeCPP += [(end - start)]

		start = pc()
		r = fib_numba(x)
		end = pc()
		timeNJIT += [(end - start)]

		start = pc()
		c = fib_py(x)
		end = pc()
		timePy += [(end-start)]
	nn = [20, 25, 30]
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

	f = Person(37)
	start = pc()
	f.fib()
	end = pc()
	t47cpp = (end - start)

	start = pc()
	t = fib_numba(37)
	end = pc()
	t47numba = (end - start)

	plt.figure(1)
	plt.plot(timeCPP, n, color='red')
	plt.plot(timeNJIT, n, color='blue')
	plt.plot(timePy, n, color='green')
	plt.savefig('Fig1.png')

	plt.figure(2)
	plt.plot(timeNJIT2, nn, color='blue')
	plt.plot(timePy2, nn, color='green')
	plt.savefig('Fig2.png')

if __name__ == '__main__':
	main()
