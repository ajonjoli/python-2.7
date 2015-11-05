# ﻿coding=utf8
#MedianString: Find a median string: a k-mer Pattern
#	that minimizes d(Pattern, Dna) among all k-mers Pattern
#	given a collection of strings Dna and an integer k
from itertools import product

def HammingDistance ( str1, str2 ):
	if len(str1) != len(str2):
		return 1000
	else:
		return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def Distance1toMany (Pattern, Dna):
	k = len(Pattern)
	TotalDistance = 0
	for string in Dna:
		MinDistance = k	#minimum possible
		for iseq in range(len(string)-k+1):
			#print string[iseq:iseq+k]
			if MinDistance > HammingDistance(Pattern,string[iseq:iseq+k]):
				MinDistance = HammingDistance(Pattern,string[iseq:iseq+k])
		TotalDistance += MinDistance
	#return sum( HammingDistance(Pattern,string) for string in Dna)
	return TotalDistance

def MedianString (Dna, k):
	distance = k*len(Dna)
	for Pattern in (''.join(list) for list in product('ACGT', repeat=k)):
		if distance > Distance1toMany (Pattern, Dna):
			#print distance, Distance1toMany(Pattern, Dna), Pattern
			distance = Distance1toMany (Pattern, Dna)
			Median = Pattern
	return Median

with open('stepic_medianstring3.txt','r') as leo:
	k = int(leo.readline().strip())
	Dna = []
	seq = leo.readline().strip()
	while seq:
		Dna.append(seq)
		seq = leo.readline().strip()
print k
#for seq in Dna:
#	print seq
	
#print MedianString(Dna,k)
Dna = ['TTACCTTAAC','GATATCTGTC','ACGGCGTTCG','CCCTAAAGAG','CGTCAGAGGT']
print Distance1toMany('GGAGGC',Dna)
