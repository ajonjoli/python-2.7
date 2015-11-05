# ﻿coding=utf8
#Ordering strings of varying length lexicographically
#Given a collection of symbols in a specific order (lexicographically) and an integer n
#return all strings of at most length n formed from the alphabet ordered lexicographically
from os import system
from itertools import product

#Leer el archivo con los DNA en formato FASTA
leo=open('rosalind_lexv2.txt','r')
symbols=leo.readline().strip().replace(' ','')
n=int(leo.readline().strip())
#symbols+='\t'
print symbols,n
leo.close()

def symbolic_key (string):
	key=[]
	for i in range(len(string)):
		key.append(symbols.find(string[i]))
	return key

#Crear combinaciones
words=[]
for nn in range(1,n+1):
	for combinacion in product(symbols, repeat=nn):
		words.append(''.join(combinacion))
lines=[]
for word in sorted(words,key=symbolic_key):
	lines.append(word+'\n')

#Escribe las combinaciones resultantes
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.writelines(lines)
scribo.close()
system('gedit rosalind_answer.txt')		#y lo escribe
