# ﻿coding=utf8
#Reverse Complement Problem
#Given a DNA string pattern return the reverse complement of that pattern
from os import system

#Leer el archivo con el DNA
leo=open('stepic_rcp3.txt','r')
dna=leo.readline().strip()	#tira la etiqeta FASTA
print len(dna)
leo.close()

complement=''
for base in dna:
	if base=='A':
		complement+='T'
	elif base=='C':
		complement+='G'
	elif base=='G':
		complement+='C'
	elif base=='T':
		complement+='A'

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.write(complement[::-1])
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
