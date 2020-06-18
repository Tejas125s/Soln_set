#!/usr/bin/env python
# coding: utf-8

# In[16]:


#chaos game for triangle
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

vertices=[(0,0),(4, 4*math.sqrt(3)),(8,0)] #Required Triangle

for i in range(1,n):
    v=random.randint(0,2) #select vertex at random
    x[i],y[i]= midpoint(vertices[v],(x[i-1],y[i-1]))

plt.scatter(x,y)
plt.show()

