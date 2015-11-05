# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
import numpy as np
leo = open('../files.txt','r')

line = leo.readline()
#histoSize = {}
#histoSize = []
sizes = []
quantity = []
#a=0

while line:
    #a+=1
    columns = line.split()
    #print columns[6],' '.join(columns[10:]).replace('\\','')
    size = int(columns[6])
    filename = ' '.join(columns[10:]).replace('\\','')
    #print size
    #if size in histoSize.keys():
        #histoSize[size] += 1
    #else:
        #histoSize[size] = 1
    #if len(histoSize) == 0:    #el primero
    if len(sizes) == 0:
        #histoSize.append([size,1])
        sizes.append(size)
        quantity.append(1)
    #elif histoSize[-1][0] == size:    # ya hay el tamaño
    elif sizes[-1] == size:
        #histoSize[-1][1] += 1
        quantity[-1] += 1
    else:    # uno más
        #histoSize.append([size,1])
        sizes.append(size)
        quantity.append(1)
    line = leo.readline()
leo.close()
#print a
#print histoSize[-20:]
#print quantity[-100:]
print sizes[0],quantity[-1]

#for s in sizes:
#    print math.log10(s),

#plt.plot(sizes[:-1],quantity[:-1])
#X = range(len(sizes))
#X2 = np.arange(0.01,len(sizes),0.01)
#plt.plot(X,quantity[::-1])
#plt.plot(X2,[math.log10(3.1)*pow(x,-0.004) for x in X2],'r')
#print [math.log(y,2) for y in [z if z!= 0 else 0.1 for z in sizes]][-50:]

X = [math.log10(x) for x in [sz if sz<>0 else 0.01 for sz in sizes]][::-1]
Y = [math.log10(y) for y in [qz if qz<>0 else 0.01 for qz in quantity]][::-1]
#print X[-50:],Y[-50:]
plt.plot(X,Y,'b+')

#plt.plot([2,7],[2.3,0.3],'r')
X=range(-1,10)
plt.plot(X,[(2*x-15.5)/-5.0 for x in X],'r')

plt.show()
#find -type f -ls | sort -k 7 -rn > files.txt