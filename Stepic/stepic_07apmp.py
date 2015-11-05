# ﻿coding=utf8
#Approximate Pattern Matching Problem
#Given a string pattern and text, and an integer d
#return all starting positions where pattern appears as substring of text with at most d mismatches
from os import system

def mismatches (strA, strB):
	if len(strA)==len(strB):
		mismatches=0
		for i in range(len(strA)):
			if strA[i]!=strB[i]:
				mismatches+=1
		return mismatches

#Leer el archivo con el DNA
leo=open('stepic_apmp4.txt','r')
pattern=leo.readline().strip()
genome=leo.readline().strip()
mismatch=int(leo.readline().strip())
leo.close()
#print pattern, len(genome), mismatch

k=len(pattern)
positions=[]
for i in range(len(genome)-k+1):
	#print genome[i:i+k]
	if mismatches(pattern,genome[i:i+k])<=mismatch:
		positions.append(i)
print len(positions)

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.write(' '.join([str(x) for x in positions]))
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
