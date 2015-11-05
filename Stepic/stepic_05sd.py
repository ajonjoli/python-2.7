# ﻿coding=utf8
#Skew diagram
#Given a string genome return all values of Skewi for i ranging from 0 to length of genome
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
#leo=open('stepic_ds2.txt','r')
#dna=leo.readline().strip()
#leo.close()
dna = leeFasta('Salmonella_enterica.txt')
print len(dna),dna[-9:]

skews=['0']
last=0
for base in dna:
	if base=='C':
		last-=1
		#skews.append(skews[-1]-1)
	elif base=='G':
		last+=1
		#skews.append(skews[-1]+1)
	skews.append(str(last))
		#skews.append(skews[-1])
#print skews

fig = plt.figure()
plt.plot(range(len(skews)),[int(x) for x in skews])
plt.xlabel('positions')
plt.ylabel('skew')
plt.show()


#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.write(' '.join(skews))
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
