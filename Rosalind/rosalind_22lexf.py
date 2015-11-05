# ﻿coding=utf8
#Enumerating k-mers lexicographically
#Given a collection of symbols in a specific order (lexicographically) and an integer
#return all strings of length n formed from the alphabet ordered lexicographically
from itertools import product
from os import system

#Leer el archivo con los DNA en formato FASTA
leo=open('rosalind_lexf2.txt','r')
symbols=leo.readline().strip().replace(' ','')
n=int(leo.readline().strip())
print symbols,n
leo.close()

#Crear combinaciones
lines=[]
for combinacion in product(symbols, repeat=n):
	#print ''.join(combinacion)
	lines.append(''.join(combinacion)+'\n')
#print lines

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.writelines(lines)
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
