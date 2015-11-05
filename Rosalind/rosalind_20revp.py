# ﻿coding=utf8
#Locating Restriction Sites
#Given a DNA string return the position (from 1 to n) and length (from 4 to 12) of every reverse palindrome.
#Reverse palindrome has all the first half complementary to the second half backwards: ATGCAT

def reverse_palindrome ( string ):
	for i in range(len(string)/2):
		if string[i]=='A' and string[-i-1]!='T':
			return False
		elif string[i]=='C' and string[-i-1]!='G':
			return False
		elif string[i]=='G' and string[-i-1]!='C':
			return False
		elif string[i]=='T' and string[-i-1]!='A':
			return False
	return True

#Leer el archivo FASTA de DNA
leo=open('rosalind_revp.txt','r')
leo.readline()	#tira la etiqeta FASTA
dna=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp:		#concatenando línea por línea
	dna+=temp
	temp=leo.readline().strip()
leo.close()
print dna,len(dna)

#Buscar palindromos de 12..4
filelines=[]
for length in range(12,3,-2):
	for begin in range(len(dna)-length+1):	#0..20	[begin,begin+1+length]
		subdna=dna[begin:begin+length]
		#print subdna,len(subdna)
		#checar si son palíndromos
		if reverse_palindrome(subdna):
			print begin+1,length#,subdna
			filelines.append(str(begin+1)+' '+str(length)+'\n')
			

scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.writelines(filelines)
scribo.close()
from os import system
system('gedit rosalind_answer.txt')		#y lo escribe
