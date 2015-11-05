# ﻿coding=utf8
#Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
#Given a string text and integers k and d return all most frequent k-mers with at most d mismatches.
from os import system
from itertools import product,combinations

def mismatches (strA, strB, d):
	if len(strA)==len(strB):
		mismatches=0
		for i in range(len(strA)):
			if strA[i]!=strB[i]:
				mismatches+=1
				d-=1
			if d<0:
				return False
		return True

#Leer el archivo con el DNA
leo=open('stepic_fwmp3.txt','r')
dna=leo.readline().strip()
k,d=[int(param) for param in leo.readline().strip().split()]
leo.close()
print dna,k,d

kmers={}
for combo in product('ACGT',repeat=k):
	kmers[''.join(combo)]=0
print len(kmers.keys())

for i in range(len(dna)-k+1):
	sub=dna[i:i+k]
	#print i,sub
#	for kmer in kmers.keys():
#		if mismatches(sub,kmer,d):
#			kmers[kmer]+=1
	for x in range(d+1):
		if x==3:
			#something
			for p1, p2, p3 in combinations(range(len(sub)),3):
				for b1 in ['A','C','G','T']:
					if sub[p1]!=b1:
						for b2 in ['A','C','G','T']:
							if sub[p2]!=b2:
								for b3 in ['A','C','G','T']:
									if sub[p3]!=b3:
										new=sub[:p1]+b1+sub[p1+1:p2]+b2+sub[p2+1:p3]+b3+sub[p3+1:]
										kmers[new]+=1
		elif x==2:
			#something
			#for p1,p2 in combinations(range(len(sub)),2):
			for p1 in range(len(sub)):
				for b1 in ['A','C','G','T']:
					if sub[p1]!=b1:
						for p2 in range(len(sub)):
							if p1<p2:
								for b2 in ['A','C','G','T']:
									if sub[p2]!=b2:
										new=sub[:p1]+b1+sub[p1+1:p2]+b2+sub[p2+1:]
										kmers[new]+=1
		elif x==1:
			#something
			#print sub
			for p in range(len(sub)):
				for b in ['A','C','G','T']:
					if sub[p]!=b:
						new=sub[:p]+b+sub[p+1:]
						kmers[new]+=1
		else:
			kmers[sub]+=1
		
#print kmers
frequents=[]
maxim=max(kmers.values())
for k,v in kmers.items():
	if v==maxim:
		frequents.append(k)
print frequents,maxim

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.writelines(' '.join(frequents))
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
