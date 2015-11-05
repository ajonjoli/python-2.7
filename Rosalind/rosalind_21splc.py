# ﻿coding=utf8
#RNA splicing
#Given a DNA string and a collection of substrings introns, all in FASTA
#return a protein string resulting from removing the introns and converting all to RNA and protein

#Leer el archivo con los DNA en formato FASTA
leo=open('rosalind_splc2.txt','r')
#Extrae la cadena de DNA
leo.readline()	#tira la etiqeta FASTA
dna=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp and temp[0]!='>':	#concatenando línea por línea
	dna+=temp
	temp=leo.readline().strip()
print dna,len(dna)
#Ahora extrae los intrones
introns=[]
intron=''
temp=leo.readline().strip()	#lee mientras no se sepa si es etiqeta FASTA o cadena adn
while temp!='':
	if temp[0]=='>':	#si etiqeta FASTA
		if intron!='':			#y ya creó una cadena dna
			introns.append(intron)	#guarda en lista de cadenas
		intron=leo.readline().strip()		#empieza nueva cadena adn
	else:
		intron+=temp	#concatena la nueva parte
	temp=leo.readline().strip()	#vuelve a leer sin saber
introns.append(intron)	#guarda el último
#print introns
leo.close()

#Quita los introns del DNA
for intron in introns:
	dna=dna.replace(intron,'')
print dna, len(dna)

#Convierte a proteína
aminobases={				#diccionario de tripletas de bases en aminoácidos
'TTT':'F', 'CTT':'L', 'ATT':'I', 'GTT':'V',
'TTC':'F', 'CTC':'L', 'ATC':'I', 'GTC':'V',
'TTA':'L', 'CTA':'L', 'ATA':'I', 'GTA':'V',
'TTG':'L', 'CTG':'L', 'ATG':'M', 'GTG':'V',
'TCT':'S', 'CCT':'P', 'ACT':'T', 'GCT':'A',
'TCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
'TCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
'TCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
'TAT':'Y', 'CAT':'H', 'AAT':'N', 'GAT':'D',
'TAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
'TAA':'X', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
'TAG':'X', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
'TGT':'C', 'CGT':'R', 'AGT':'S', 'GGT':'G',
'TGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
'TGA':'X', 'CGA':'R', 'AGA':'R', 'GGA':'G',
'TGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}
protein=''
for icodon in range(0,len(dna),3):
	#print icodon,'-',
	codon=dna[icodon:icodon+3]
	if aminobases[codon]=='X':
		break
	else:
		protein+=aminobases[codon]
print protein,len(protein)

			
#Escribir la proteína resultante
scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.write(protein)
scribo.close()
from os import system
system('gedit rosalind_answer.txt')		#y lo escribe
