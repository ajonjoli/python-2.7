# ﻿coding=utf8
import math as math
import numpy as np
from scipy import special as sp
import matplotlib.pyplot as plt

def NormalDistribution (xs, mean=0, stdev=1):
	ys = []
	for x in xs:
		# f(x,mean,stdev)=[1/stdev*sqrt(2pi)]e^[-(x-mean)^2/(2stdev^2)]
		y = 1.0 / (stdev * math.sqrt(2*math.pi))
		exp = - (x-mean)**2 / (2.0*stdev**2)
		#print y, exp
		y *= (math.e ** exp)
		ys.append(y)
	return ys

def BetaDistribution (xs, alpha=0, beta=1):
	ys = []
	for x in xs:
		# 1/B(a,b) * x^a-1 * (1-x)^(b-1)
		y = (x ** (alpha-1)) * ((1-x) ** (beta-1))
		#BetaInv = mt.factorial(alpha+beta-1) / ( mt.factorial(alpha-1)*mt.factorial(beta-1) )
		BetaInv = 1.0 / sp.beta(alpha,beta)
		#print y, FuncBeta
		y *= BetaInv
		ys.append(y)
	return ys

def Graphic (x,y):
	plt.plot(x,y,'.')
	plt.show()

#------------------------------------------------------
def sdnorm(z):
	"""	Standard Normal pdf (Probability Density Function)	mean = 0, stdev = 1	"""
	return math.exp(-z*z/2.) / math.sqrt(2*math.pi)

def MH (n):
	current = 0.0
	vector = [current]
	#random innovation, uniform proposal distribution
	innov = np.random.uniform(-1,1,n)
	#print innov
	for i in xrange(1,n):
		candidate = current + innov[i] #candidate
		aprobal = min([ 1.0, sdnorm(candidate)/sdnorm(current) ]) #acceptance probability
		u = np.random.uniform(0,1)
		if u < aprobal:	#change current
			current = candidate
			vector.append(current)
	return vector

def evalLogLikelihood (params, D, N, Mmin, Mmax):
	alpha = params[0]
	c = (1.0 - alpha) / ( math.pow(Mmax,1.0-alpha) - math.pow(Mmin,1.0-alpha) )
	return N*math.log(c) - alpha*D


#plotting the results:
#theoretical curve
n = 100000
vec = MH(n)
#print vec
plt.subplot(211)
plt.title('Metropolis-Hastings')
plt.plot(vec)

plt.subplot(212)
#divide the numbers vec in 100 bins with freq y and then normalize so the sum of votes is 1
plt.hist(vec, bins=100, normed=1)

xs = np.arange(-3,3,.1)
ys = [sdnorm(x) for x in xs]
# for i in range(len(xs)):
# 	print xs[i],ys[i]
plt.plot(xs,ys,'r.')
plt.ylabel('Freqs')
plt.xlabel('x')
plt.legend(('PDF','Samples'))
plt.show()
#------------------------------------------------------

#print NormalDistribution([1], 0, 1)
#Graphic(range(10),range(10,0,-1))
xs = np.linspace(0.0, 1.0, 500)
ys = BetaDistribution(xs,2,3)
print len(xs), sum(ys)
#Graphic( xs, ys )