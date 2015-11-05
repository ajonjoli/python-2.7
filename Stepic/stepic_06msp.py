# ﻿coding=utf8
#Minimum Skew Problem
#Given a string genome return all i of Skewi for i ranging from 0 to length of genome where skew is the minimum
from os import system
import matplotlib.pyplot as plt

def leeFasta ( path ):
	with open(path,'r') as leo:
		leo.readline()	#throw fasta label
		seq = ''
		tmp = leo.readline().strip()
		while tmp:
			seq += tmp
			tmp = leo.readline().strip()
	return seq

#Leer el archivo con el DNA
#leo=open('stepic_msp3.txt','r')
#dna=leo.readline().strip()
#leo.close()
dna = leeFasta('Salmonella_enterica.txt')
#print dna,len(dna)

skews=[0]
last=0
for base in dna:
	if base=='C':
		last-=1
		#skews.append(skews[-1]-1)
	elif base=='G':
		last+=1
		#skews.append(skews[-1]+1)
	skews.append(last)
		#skews.append(skews[-1])
#print skews

#Encontrar las posiciones del elemento menor
minim=min(skews)
positions=[]	#[i for i in range(len(skews)) if skews[i]==minim]
for i in range(len(skews)):
	if skews[i]==minim:
		positions.append(i)
print positions

fig = plt.figure()
plt.plot(range(len(skews)),skews)
plt.xlabel('positions')
plt.ylabel('skew')
plt.show()

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.write(' '.join([str(x) for x in positions]))
scribo.write('\n'+dna[positions[0]-500:positions[-1]+500])
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
