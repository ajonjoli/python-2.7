# ﻿coding=utf8
#Cuenta el número de cada base: A, C, G, T
intro=open('rosalind_dna.txt','r')
A=0
C=0
G=0
T=0
strand=intro.read(1)
while strand!='':
	if strand=='A':
		A+=1
	elif strand=='C':
		C+=1
	elif strand=='G':
		G+=1
	elif strand=='T':
		T+=1
	strand=intro.read(1)
print A,C,G,T
raw_input()
gardo=open('rosalind_dna_answer.txt','w')
gardo.write(str(A)+' '+str(C)+' '+str(G)+' '+str(T))
intro.close()
gardo.close()
