# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 06:55:26 2022

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

aci = float (input ('aci = ')) # initial acceleration
aci = mm_to_meter(aci)

qf = float (input ('qf = ')) # final position
qf = mm_to_meter(qf)

vf = float (input ('vf = ')) # final velocity
vf = mm_to_meter(vf)

acf = float (input ('acf = ')) # final acceleration
acf = mm_to_meter(acf)

ti= float (input ('ti = ')) # initial time
tf= float (input ('tf = ')) # final time


# Quintic Polynnomial 
#Solve the solution for q(t) = c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 +c5*t**5

M = [[1, ti, ti**2, ti**3, ti**4, ti**5],
     [0, 1, 2*ti, 3*ti**2, 4*ti**3, 5*ti**4],
     [0, 0, 2, 6*ti, 12*ti**2, 20*ti**3],
     [1, tf, tf**2, tf**3, tf**4, tf**5],
     [0, 1, 2*tf, 3*tf**2, 4*tf**3, 5*tf**4],
     [0,0,2,6*tf, 12*tf**2, 20*tf**3]]

M = np.matrix(M)

b= [[qi], [vi], [aci], [qf], [vf], [acf]]

a = np.linalg.inv(M) * b

x = np.arange(ti,tf,0.05) 

def qt(t,c0,c1,c2,c3,c4,c5):
    return c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 +c5*t**5

y = qt(x,a[0,0],a[1,0],a[2,0],a[3,0],a[4,0],a[5,0])

plt.figure()
plt.plot(x,y,'b',linestyle='-')
plt.text(1,1.5,'q(t) = c0 + c1*t + c2*t**2 + c3*t**3 + c4*t**4 +c5*t**5')
plt.grid(True)
plt.show()