# ﻿coding=utf8
#Calculate probability that substring pattern appears t or more times in a string of length 25 formed from an alphabet of A letters
from itertools import product
from scipy import special

def Probability (N, A, pattern, t):
	chars=''
	for number in range(A if A<=10 else 10):
		chars += str(number)
	#print chars
	Strings = []
	numerator = 0
	for string in product(chars, repeat=N):
		string = ''.join(string)
		Strings.append(string)
		if pattern in string:
			numerator += 1
	print Strings[0:20]
	denominator = len(Strings)*1.0
	print numerator,'\t',numerator/denominator

#def ApproximatedProbability (N, A, pattern, t):
#	k = len(pattern)
#	print k
#	denominator = 1.0*A**(t*k)
#	numerator = special.binom((N-(t*(k-1))),t)
#	print (N-(t*(k-1))), numerator
#	print 'Result:',numerator,'/',denominator,'=',
#	return numerator / denominator

def ApproximatedProbability (N, A, pattern, t):
	k = len(pattern)
	n = N - (t*k)
	print k,n
	denominator = A**N
	numerator = special.binom(n+t,t)*A**n
	print special.binom(n+t,t),A**n
	print 'Result:',numerator,'/',denominator,'=',
	return numerator / denominator

print ApproximatedProbability (25, 2, '01', 1)
print ApproximatedProbability (7, 3, '01', 2)
#print Probability (25, 2, '01', 1)
