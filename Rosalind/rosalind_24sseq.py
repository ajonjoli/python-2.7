# ﻿coding=utf8
#Finding a spliced motif
#Given two DNA strings s & t return one collection of indices of s per each symbol of t as a subsequence of s, return only one of the solutions.
from os import system

#Leer el archivo con el DNA en formato FASTA
leo=open('rosalind_sseq2.txt','r')
leo.readline()	#tira la etiqeta FASTA
seqdna=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp and temp[0]!='>':	#concatenando línea por línea
	seqdna+=temp
	temp=leo.readline().strip()
subdna=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp:	#concatenando línea por línea
	subdna+=temp
	temp=leo.readline().strip()
print seqdna,len(seqdna)
print subdna,len(subdna)
leo.close()

#buscar las posiciones
indices=[]
lines=[]
ini=0
for base in subdna:
	ini=seqdna.find(base,ini+1)
	indices.append(ini)
	#print ini
if -1 in indices:
	print 'no hay subsecuencia posible'
else:
	for index in indices:
		print index+1
		lines.append(str(index+1)+'\n')
	#print lines

	#Escribe las combinaciones resultantes
	scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
	scribo.writelines(lines)
	scribo.close()
	system('gedit rosalind_answer.txt')		#y lo escribe
