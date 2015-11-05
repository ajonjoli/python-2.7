# ﻿coding=utf8
# Generate the d-neighborhood Neighbors(Pattern, d), the set of all k-mers whose Hamming distance from Pattern does not exceed d.
# MotifEnumeration (dna,k,d) gets all the k-mers with at least d mutations that appears in all the strings in dna
from os import system
BASES = ('A','C','G','T')

def HammingDistance ( str1, str2 ):
	if len(str1) != len(str2):
		return 1000
	else:
		return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def DifferentBases (FirstBase):
	for DiffBase in BASES:
		if DiffBase != FirstBase:
			yield DiffBase
	#for DiffBase in ('A','C','G','T') if DiffBase != FirstBase

def ImmediateNeighbors (pattern):
	Neighborhood = [pattern]
	for i in range(len(pattern)):
		for NewBase in DifferentBases(pattern[i]):
			Neighbor = pattern[:i]+NewBase+pattern[i+1:]
			#print Neighbor
			Neighborhood.append(Neighbor)
	return Neighborhood

def Neighbors (pattern, d):
	if d == 0:
		return (Pattern)
	if len(pattern) == 1:
		return BASES
	Neighborhood = []
	#print pattern[1:]
	SuffixNeighbors = Neighbors(pattern[1:], d)
	#print SuffixNeighbors,pattern[1:]
	for rest in SuffixNeighbors:
		#print HammingDistance(pattern[1:],rest),d
		if HammingDistance(pattern[1:], rest) < d:
			for base in BASES:
				#print base+rest
				Neighborhood.append(base+rest)
		else:
			#print pattern[0]+rest
			Neighborhood.append(pattern[0]+rest)
	return Neighborhood

def CheckMotif (pattern, dna, d):
	numseqs = len(dna)
	found = 0
	for seq in dna:
		for ikstring in range(len(seq)-len(pattern)+1):
			kstring = seq[ikstring:ikstring+len(pattern)]
			if HammingDistance(pattern,kstring) <= d:
				found += 1
				break
	return True if found >= numseqs else False

def MotifEnumeration (dna, k, d):
	patterns = set()
	for string in dna:
		for ikstring in range(len(string)-k+1):
			kstring = string[ikstring:ikstring+k]
			for kmer in Neighbors(kstring,d):
				if CheckMotif (kmer, dna, d):
					patterns.update([kmer])
	return patterns

#print [x for x in DifferentBases('T')]
#print ImmediateNeighbors('ACGT')
#print HammingDistance('ACGT','TCGA'), HammingDistance('ACGT','TGCA'), HammingDistance('ACGT','AAAAA')
#print Neighbors ('ACG',1)
seqs = Neighbors ('ACGT',2)
print seqs,len(seqs)
seqs = Neighbors ('CACCAATG',3)

dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
print MotifEnumeration (dna, 3, 1)
dna = [
'GTCACGGGGAGACCCGCCTAAGGCG',
'ACATGTTGTTGACTGGCATATCCCT',
'TAGTATAATTCGTTAACCTACGTGC',
'GTATTGCGTAAGTGAGACAGCTTCA',
'TTTCGCCGTATATCCGAGCAGTACG',
'AGCTGTACCGCAGTACCCTAATCGG']
seqs = MotifEnumeration (dna, 5, 2)

with open('rosalind_answer.txt','w') as scribo:
	for string in seqs:
		scribo.write(string+' ')
system('gedit rosalind_answer.txt')		#y lo escribe
