import numpy as np
import math

def func_example1(x):
  return x - 1.5

def func_example2(x):
  return x**3 - 4 * x

def func_example3(x):
  return math.log(x+8)

def func_example4(x):
  return np.cos(x)

def func_example5(x):
  return math.e**x + math.e**(-x) - 2.2

def func_example6(x):
  return - x**2 + math.e**x

def func_example7( x ):
  V0 = 10
  g = 9.81
  x_trav = 10
  return x_trav - V0 **2 * np.sin( 2 * x ) / g

def func_example8( x ):
  V0 = 10
  g = 9.81
  theta = np.pi/3
  return x * np.tan( theta) - g * x**2 / (2 * V0**2 * np.cos(theta)**2 )