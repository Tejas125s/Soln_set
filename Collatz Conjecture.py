#!/usr/bin/env python
# coding: utf-8

# In[16]:


import math
import matplotlib.pyplot as plt

def collatz(x):
    A=[x]
    while(x!=1):    
        if(x%2==0):
            A.append(x/2)
            x=x/2
        else:
            A.append((3*x)+1)
            x=(3*x)+1
    plt.plot(list(range(0,len(A))), A)
    return A
L = int(input('Lower limit for range:'))
U = int(input('Upper limit for range:'))
n=U-L+1
X=list(range(L,U+1))
B=[[],0]
for i in X:
    B[0].extend(collatz(i))
    if(B[1]<len(collatz(i))):
        B[1]=len(collatz(i))
plt.show()
print(B)
maxi=max(B[0]) #calculating bins
print (maxi)
rng=maxi-1
obs=len(B[0])
inter= math.sqrt(obs)
width=(rng/inter)
c=0
D=[]
while(c<maxi):
    D.append(c)
    c=c+width
D.append(c)
plt.hist(B[0],bins=D)
plt.show()

