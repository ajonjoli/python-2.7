# ﻿coding=utf8
# Neighbors
from os import system
BASES = ('A','C','G','T')

def Neighbors (pattern, d):
	if d == 0:
		return [pattern]
	if len(pattern) == 1:
		return ['A', 'C', 'G', 'T']
	Neighborhood = []
	SuffixNeighbors = Neighbors(pattern[1:], d)
	for Text in SuffixNeighbors:
		if HammingDistance(pattern[1:], Text) < d:
			for x in ['A','C','G','T']:
				Neighborhood.append(x+Text)
		else:
			Neighborhood.append(Pattern[0]+Text)
	return Neighborhood

def SymbolToNumber (symbol):
	return BASES.index(symbol)
	
def NumberToSymbol (number):
	return BASES[number]

#def PatternToNumber (seq):
#	value = 0
#	for ichar in range(len(seq)):
#		char = seq[::-1][ichar]
#		#print char
#		#if char=='A': +zero
#		if char=='C':
#			#print ichar,4**ichar
#			value += 4**ichar
#		elif char=='G':
#			#print 4**ichar,2*(4**ichar)
#			value += 2*(4**ichar)
#		elif char=='T':
#			#print 4**ichar,3*(4**ichar)
#			value += 3*(4**ichar)
#	return value

def PatternToNumber (seq):
	if seq == '':
		return 0
	#print 4*PatternToNumber(seq[0:-1]),seq[-1]
	return (4*PatternToNumber(seq[0:-1])) + SymbolToNumber(seq[-1])
	
#def NumberToPattern (number, k):
#	seq = ''
#	for ik in range(k):
#		ichar = number%4
#		number = number/4
#		#print ichar
#		if ichar==0:
#			seq = 'A' + seq
#		elif ichar==1:
#			seq = 'C' + seq
#		elif ichar==2:
#			seq = 'G' + seq
#		elif ichar==3:
#			seq = 'T' + seq
#		#print value
#	return seq

def NumberToPattern (number, k):
	if k == 1:
		return NumberToSymbol(number)
	return NumberToPattern(number/4,k-1) + NumberToSymbol(number%4)

def ComputingFrequencies (Text, k):
	counts = [0]* (4**k)
	#print counts,len(counts)
	for kmer in range(len(Text)-k+1):
		pattern = Text[kmer:kmer+k]
		#print pattern
		counts[PatternToNumber(pattern)] += 1
	return counts
	
def FindingFrequentWordsBySorting (Text, k):
	FrequentPatterns = []
	IndexCount = []
	order = range(len(Text)-k+1)
	for i in order:
		Pattern = Text[i:i+k]
		IndexCount.append([PatternToNumber(Pattern),1])
	IndexCount.sort()
	for i in order[1:]:
		if IndexCount[i][0] == IndexCount[i-1][0]:
			IndexCount[i][1] = IndexCount[i-1][1]+1
	maxCount = max(IndexCount,key=lambda x:x[1])[1]
	for i in order:
		if IndexCount[i][1] == maxCount:
			FrequentPatterns.append( NumberToPattern(IndexCount[i][0],k) )
	return FrequentPatterns

def ClumpFinding (Genome, k, t, L):
	FrequentPatterns = []
	order = range(len((4**k)-1))
	Clump = [0]*len(order)
	Text = Genome[0:L]
	FrequencyArray = ComputingFrequencies(Text, k)
	for i in order:
		if FrequencyArray[i] >= t:
			Clump[i] = 1
	for i in range(1,len(Genome)-L+1):
		FirstPattern = Genome[i-1:k]
		j = PatternToNumber(FirstPattern)
		FrequencyArray[j] -= 1
		LastPattern = Genome[i+L-k:k]	#i+L-k:i+L
		j = PatternToNumber(LastPattern)
		FrequencyArray[j] += 1
		if FrequencyArray[j] >= t:
			Clump[j] = 1
	for i in order:
		if Clump[i] = 1
			Pattern = NumberToPattern(i,k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns

print 'GT',PatternToNumber('GT')	#11
print 'ATGCAA',PatternToNumber('ATGCAA')	#912
print 'CTTCTCACGTACAACAAAATC',PatternToNumber('CTTCTCACGTACAACAAAATC')	#2161555804173
print 'GATTGACGGGATGTACCGG',PatternToNumber('GATTGACGGGATGTACCGG')	#154109799514

print NumberToPattern(11, 2)	#GT
print NumberToPattern(5437, 7)	#CCCATTC
print NumberToPattern(5437, 8)	#ACCCATTC
print NumberToPattern(45,4)		#AGTC
print NumberToPattern(7964,10)

#Leer el archivo con el DNA
with open('stepic_cfa.txt','r') as leo:
	seq = leo.readline().strip()
	k = int(leo.readline().strip())
print seq,k
print FindingFrequentWordsBySorting (seq, k)
result = ' '.join(str(n) for n in ComputingFrequencies (seq, k))
print result

#with open('rosalind_answer.txt','w') as scribo:
#	scribo.write(result)
#system('gedit rosalind_answer.txt')		#y lo escribe
