# ﻿coding=utf8
#Perfect matchings and RNA secondary structures
#Given an RNA string with same ocurrences of A as U, and the same of C as G.
#Return the total possible number of perfect matchings of basepair edges
from math import factorial

#Leer el archivo con el DNA en formato FASTA
leo=open('rosalind_pmch2.txt','r')
leo.readline()	#tira la etiqeta FASTA
dna=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp:	#concatenando línea por línea
	dna+=temp
	temp=leo.readline().strip()
leo.close()
print dna,len(dna)

#Contar las A y C
print factorial(dna.count('A')) * factorial(dna.count('C'))
#Calcular y mostrar producto de factoriales!
