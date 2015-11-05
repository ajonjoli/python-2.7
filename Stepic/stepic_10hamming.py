# ﻿coding=utf8
# Compute the Hamming distance between two strings of equal length

#Leer el archivo con el DNA
leo=open('stepic_hamming2.txt','r')
str1=leo.readline().strip()
str2=leo.readline().strip()
leo.close()

def hammingDistance ( str1, str2 ):
	hamming = 0
	for i in range(len(str1)):
		if str1[i]!=str2[i]:
			hamming += 1
	return hamming

print hamming
