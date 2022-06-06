# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 03:28:54 2022

@author: Acer
"""

import numpy as np
import matplotlib.pyplot as plt

#degrees to radian converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

qi = float (input ('qi = ')) # initial position
qi = mm_to_meter(qi)

vi = float (input ('vi = ')) # initial velocity
vi = mm_to_meter(vi)

qf = float (input ('qf = ')) # final position
qf = mm_to_meter(qf)

vf = float (input ('vf = ')) # final velocity
vf = mm_to_meter(vf)

ti= float (input ('ti = ')) # initial time
tf= float (input ('tf = ')) # final time
#Cubic 
#Solve the solution for q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

x = np.arange(ti,tf,0.05) 

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

y = cubic(x,qi,qf,tf)

plt.figure()
plt.plot(x,y,'b',linestyle='-')
plt.text(1,1.5,'q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3')
plt.grid(True)
plt.show()