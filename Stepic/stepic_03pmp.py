# ﻿coding=utf8
#Pattern Matching Problem
#Given two DNA strings pattern and genome return all starting positions where pattern appears as substring of genome. Starting on position 0.
from os import system

#Leer el archivo con el DNA
leo=open('stepic_pmp.txt','r')
patt=leo.readline().strip()
genome=leo.readline().strip()
print len(patt),len(genome)
leo.close()

pos=-1
posiciones=[]
Found=True
while Found==True:
	pos=genome.find(patt,pos+1)
	if pos==-1:
		Found=False
	else:
		posiciones.append(str(pos))
	#print 'post',pos
print len(posiciones)

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.write(' '.join(posiciones))
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
