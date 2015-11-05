# ﻿coding=utf8
#Clump Finding Problem
#Given a string genome and integer k, L, t.
#Return all distinct k-mers forming (L,t)-clumps in Genome.
from os import system

#Leer el archivo con el DNA
leo=open('stepic_cfp3.txt','r')	#stepic_cfp3.txt	E-coli.txt
dna=leo.readline().strip()
k,L,t=[int(param) for param in leo.readline().strip().split()]
#print dna
print k,L,t
leo.close()

kmers={}
clumps=set()
print len(dna[0:L]),dna[0:L]
for i in range(L-k+1):
	kmer=dna[i:i+k]
	if kmers.has_key(kmer):	# and kmers[kmer]<=t:
		kmers[kmer]+=1
	else:	#if kmer not in clumps:
		kmers[kmer]=1
#print kmers
for kmer in kmers.keys():
	if kmers[kmer]>=t:
		clumps.update([kmer])
for i in range(1,len(dna)-L+1):
	#print dna[i:i+L]
	rem=dna[i-1:i-1+k]
	add=dna[i+L-k:i+L]
	#print rem,add
	#raw_input()
	kmers[rem]-=1
	if kmers.has_key(add):
		kmers[add]+=1
		if kmers[add]>=t and add not in clumps:
			clumps.update([add])
	else:
		kmers[add]=1
print clumps,len(clumps)

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.write(' '.join(clumps))
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
