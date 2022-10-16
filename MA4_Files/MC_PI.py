"""
Solution to MA4, 1, Parallellprogrammering
Student: Elis Uebel
Mail: elis.uebel.4496@student.uu.se
Reviewed by: 
Review Date:
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import concurrent.futures as future
from time import perf_counter as pc

MC_iterations = [1000, 10000, 100000]


n_c_x = []
n_c_y = []
n_o_x = []
n_o_y = []

PI_est = []

for z in MC_iterations:
    n_c = []
    n_out = []

    x_c_temp = []
    y_c_temp = []
    x_o_temp = []
    y_o_temp = []

    for z0 in range(z):
        x = np.random.uniform(low=-1, high=1)
        y = np.random.uniform(low=-1, high=1) 
        if x*x + y*y <= 1:
            n_c += [x, y]
            x_c_temp += [x]
            y_c_temp += [y]
        else:
            n_out += [x, y]
            x_o_temp += [x]
            y_o_temp += [y]

    n_c_x += [x_c_temp]
    n_c_y += [y_c_temp]
    n_o_x += [x_o_temp]
    n_o_y += [y_o_temp]
    PI_est += [4*len(n_c)/(len(n_c) + len(n_out))]

print(PI_est)

plot_indx = 2

plt.scatter(n_c_x[plot_indx], n_c_y[plot_indx],color='red')
plt.scatter(n_o_x[plot_indx], n_o_y[plot_indx],color='blue')
#plt.show()


G = lambda x : math.gamma(x/2 + 1)

def leq1(x):
    if x <= 1:
        return True
    else:
        return False

def hypersphere(n, d):
    """
    points = []
    for a in range(n):
        points += [sum([np.random.uniform(low=-1, high=1)**2 for i in range(d)])]
    """

    start = pc()

    points = [sum([np.random.uniform(low=-1, high=1)**2 for i in range(d)]) for ii in range(n)]
    p_in = list(filter(leq1, points))

    PI = (G(d)*(2**d)*(len(p_in)/len(points)))**(2/d)

    V_theo = (math.pi**(d/2))/G(d)   

    V_calc = (2**d)*(len(p_in)/len(points))

    end = pc()

    print('Fraction V_calc/V_theo = ' + str(V_calc/V_theo))
    print('Time elapsed: ' + str(end- start) + 'seconds' + '\n')

hypersphere(100000, 11)


def hyper_parallell(n, d):
    """
    points = []
    for a in range(n):
        points += [sum([np.random.uniform(low=-1, high=1)**2 for i in range(d)])]
    """

    points = [sum([np.random.uniform(low=-1, high=1)**2 for i in range(d)]) for ii in range(n)]
    p_in = list(filter(leq1, points))

    
    return [p_in, points]

with future.ProcessPoolExecutor() as ex:
    n = []
    d = []

    nvar = 100000
    dvar = 11

    start = pc()

    for x in range(10):
        n += [nvar]
        d += [dvar]

    result = ex.map(hyper_parallell, n, d)

    p_in = []
    points = []

    for r in result:
        p_in += r[0]
        points += r[1]
    
    d = d[0]

    n = n[0]*len(n)

    V_theo = (math.pi**(d/2))/G(d)   

    V_calc = (2**d)*(len(p_in)/len(points))

    end = pc()
    
    print('Parallel fraction V_calc/V_theo = ' + str(V_calc/V_theo))
    print('Time elapsed: ' + str(end- start) + 'seconds')
