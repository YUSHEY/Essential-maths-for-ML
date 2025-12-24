#declaring a funcn with 2 independent var in Python
from sympy import *
from sympy.plotting import plot3d
x,y= symbols('x y')
f=2*x+3*y
plot3d(f)