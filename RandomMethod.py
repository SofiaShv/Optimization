import random
import math
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

def norm (point): #norm of the point
    return point[0]*point[0] + point[1]*point[1]

# first random coordinate
x1 = random.uniform(-100, 100)
x2 = random.uniform(-100, 100)
first_point = [x1, x2]

F1 = func (first_point)
new_point = first_point

i=0
const = 1_000_000
eps =0.0001
function_value = [F1]
a=[i]

while i < const :
#while norm(gradient(new_point)) > eps:

    # random coordinate №i
    y1 = random.uniform(-100, 100)
    y2 = random.uniform(-100, 100)
    new_point = [y1, y2]

    #condition of replacing minimal element
    if func (new_point) < F1:
        F1 = func (new_point)
        function_value.append(func(new_point))
        a.append(i)

    i= i+1

plt.plot (function_value)
plt.show ()

print (F1)