#!/usr/bin/env python
# coding: utf-8

# In[16]:


import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#function for calculating AGM
def AGM(b,c):
    a=b
    g=c
    while (abs(a-g)> 1.e-7): #to limit iterations
        a= ((b+c)/2)
        g= (math.sqrt(b*c))
        b=a
        c=g
    return(a)

L = int(input('Lower limit for range:'))
U = int(input('Upper limit for range:'))
n=U-L+1

#3d plot of values
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection ='3d')
X=[]
Y=[]
#list of number sets
for i in range(L,U+1):
    for j in range (0,n):
        X.append(i)

for i in range(0,n):
    for j in range(L,U+1):
        Y.append(j)

result = []
for i in range(L,U+1):
    for j in range(L,U+1):
        result.append(AGM(i,j))
print(X)
print(Y)

ax.scatter(X,Y,result)
ax.set_xlabel('Range of numbers')
ax.set_ylabel('Range of numbers')
ax.set_zlabel('Range of AGM')
plt.show()

