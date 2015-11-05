# ﻿coding=utf8
#Frequent Words Problem
#Given a string text and an integer k return all most frequent k-mers
from os import system

#Leer el archivo con el DNA
with open('stepic_fwp.txt','r') as leo:
	dna=leo.readline().strip()
	n=int(leo.readline().strip())
print dna,len(dna),n

kmers={}
for i in range(len(dna)-n+1):
	if kmers.has_key(dna[i:i+n]):
		kmers[dna[i:i+n]]+=1
	else:
		kmers[dna[i:i+n]]=1
#print kmers
winners = [k for k,v in kmers.items() if v==max(kmers.values())]
print winners
line = ' '.join(winners)

#Escribe las combinaciones resultantes
with open('rosalind_answer.txt','w') as scribo:	#guardar en un archivo
	scribo.writelines(line)
system('gedit rosalind_answer.txt')		#y lo escribe
