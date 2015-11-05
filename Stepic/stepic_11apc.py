# ﻿coding=utf8
# Implement ApproximatePatternCount given a Text, a pattern and integer d
# Count hamming distance between pattern and every k-mer substring of Text.

def HammingDistance ( str1, str2 ):
	hamming = 0
	for i in range(len(str1)):
		if str1[i]!=str2[i]:
			hamming += 1
	return hamming

def ApproximatePatternCount ( text, pattern, d):
	count = 0
	k = len(pattern)
	for i in range(len(text)-k+1):
		kmer = text[i:i+k]
		#print kmer
		if HammingDistance(pattern,kmer) <= d:
			count += 1
			print kmer, count
	return count

#Leer el archivo con el DNA
leo=open('stepic_apc2.txt','r')
text=leo.readline().strip()
pattern=leo.readline().strip()
d=int(leo.readline().strip())
leo.close()
print pattern,d

print ApproximatePatternCount(text,pattern,d)
