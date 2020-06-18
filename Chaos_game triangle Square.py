#!/usr/bin/env python
# coding: utf-8

# In[4]:


#chaos game for triangle and square, can be done by making a few edits to the code
import numpy
import matplotlib.pyplot as plt
import math
import random

#function for midpoint

def midpoint(a,b):
    return ((a[0]+b[0])/2, (a[1]+b[1])/2) 

n = int(input("Enter No. of iterations to perform:"))
#coordinates

x=numpy.zeros(n) 
y=numpy.zeros(n)

#point selection

x[0]=random.random() 
y[0]=random.random()
prev=0
vertices=[(0,0),(1,0),(0,1),(1,1)] #vertices
value=int(input("Enter 2 for triangle, 3 for square"))
if(value==3):
    for i in range(1,n):
        while(v==prev):
            v=random.randint(0,3) #select vertex at random
            # 3 for square
        x[i],y[i]= midpoint(vertices[v],(x[i-1],y[i-1]))
        prev=v
    plt.scatter(x,y)
    plt.xlim(-0.3,1.3)
    plt.ylim(-0.3,1.3)
    plt.show()
else:
    for i in range(1,n):
        v=random.randint(0,2)# 2 for triangle.
        x[i],y[i]= midpoint(vertices[v],(x[i-1],y[i-1]))
    plt.scatter(x,y)
    plt.xlim(-0.3,1.3)
    plt.ylim(-0.3,1.3)
    plt.show()

