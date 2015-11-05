# -*- coding: utf-8 -*-
#Finding a Shared Spliced Motif
#Given two DNA strings s, t in FASTA format
#Return a longest common subsequence s, t. If more than one, return any one.
from os import system
import itertools
	
#Leer el archivo con los DNA en formato FASTA
leo=open('rosalind_lcsq2.txt','r')
leo.readline()	#tira la etiqeta FASTA
dna1=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp and temp[0]!='>':	#concatenando línea por línea
	dna1+=temp
	temp=leo.readline().strip()
dna2=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp:	#concatenando línea por línea
	dna2+=temp
	temp=leo.readline().strip()
leo.close()
print dna1,len(dna1)
print dna2,len(dna2)

#Dynamic programming

#Declara una matriz de 0s
#lengths=[[0 for j in range(len(dna1)+1)] for i in range(len(dna2)+1)]
lengths=[[0]*(len(dna2)+1) for i in range(len(dna1)+1)]
#Llena la matriz recorriendo ambas secuencias
for i in range(len(dna1)):
	for j in range(len(dna2)):
		if dna1[i]==dna2[j]:
			lengths[i+1][j+1]=lengths[i][j]+1
		else:
			lengths[i+1][j+1]=max(lengths[i+1][j],lengths[i][j+1])
#for x in lengths:
#	print x

#Recorre la matriz de fin a inicio buscando con los números secuenciales los caracteres comunes
subsequence=''
x, y = len(dna1), len(dna2)
while x!=0 and y!=0:
	if lengths[x][y]==lengths[x-1][y]:
		x-=1
	elif lengths[x][y]==lengths[x][y-1]:
		y-=1
	else:
		assert dna1[x-1]==dna2[y-1]
		subsequence=dna1[x-1]+subsequence
		x-=1
		y-=1
print subsequence,len(subsequence)

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.writelines(subsequence)
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
