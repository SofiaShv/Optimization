from this import i
from typing import List

import math
import csv
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# змінює стиль графіків зі стандартного, на Bayesian Methods for Hackers
plt.style.use('bmh')

def func(point):
    return point[0]*point[0] + 3*point[1]*point[1] + math.cos (point[0]+point[1])  # calculation of f(x)

def gradient (point) -> list:
    grad = [2 * point[0] + math.cos(point[0] + point[1]), 6 * point[1] + math.cos(point[0] + point[1])] # gradient of f(x)
    return grad

def h (k): # h(k) for calculation x(k+1)
    if (k<20):
        return 2/100
    else:
        return 1/k

def norm (point): #norm of the point
    return point[0]*point[0] + point[1]*point[1]

def b (point1, point2): # b(k) for calculation p(k+1)
    return norm(gradient(point1)) / norm(gradient(point2))

k=0
next_point = [100,100]
p=gradient(next_point)
function_value=[next_point]

eps = 0.0001
a=[0]

while norm(gradient(next_point)) > eps:

#while k<100_000:

    first_point = [next_point[0], next_point[1]] #x(k)
    next_point = [first_point[0]+h(k)*p[0], first_point[1]+h(k)*p[1]] #x(k+1)
    p = [gradient(next_point)[0] - b(next_point,first_point)*p[0], gradient(next_point)[1] - b(next_point,first_point)*p[1]] #p(k+1)
    k=k+1
    #if k<400 :
    function_value.append(next_point)
    a.append(k)


plt.plot (a, function_value)
plt.show ()

print (func(next_point))