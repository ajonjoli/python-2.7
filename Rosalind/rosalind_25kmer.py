# ﻿coding=utf8
#k-mer composition
#Given a DNA string, count its 4-mer composition
from os import system
from itertools import product

#Leer el archivo con el DNA en formato FASTA
leo=open('rosalind_kmer2.txt','r')
leo.readline()	#tira la etiqeta FASTA
dna=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp:		#concatenando línea por línea
	dna+=temp
	temp=leo.readline().strip()
print dna,len(dna)
leo.close()

#Crear el diccionario de 4-mers
dmers={}
line=''
for kmer in product('ACGT',repeat=4):
	#print ''.join(kmer)
	dmers[''.join(kmer)]=0
#Contar los 4-mers presenten en el DNA
for imer in range(len(dna)-4+1):
	#print dna[imer:imer+4]
	dmers[dna[imer:imer+4]]+=1
#Ordenarlos y ordenarlos
for kmer in sorted(dmers.keys()):
	line+=str(dmers[kmer])+' '
	print dmers[kmer],

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.write(line[:-1])
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
