# ﻿coding=utf8
# Open reading frames
# Dada una cadena de ADN en formato FASTA devolver todas las proteinas que pueden salir en formato ORF de dicha cadena
# el formato ORF inicia con el codon de inicio, termina con algun codon de fin y no tiene ningun codon de fin en medio
# recordar que pueden salir proteínas de la cadena inicial y de su complemento

#lee archivo de proteínas
leo=open('rosalind_orf2.txt','r')
leo.readline()	#tira la etiqeta FASTA
dna=''			#guarda la cadena DNA del archivo a la variable
temp=leo.readline().strip()
while temp:		#concatenando línea por línea
	dna+=temp
	temp=leo.readline().strip()
leo.close()

aminos=[]				#guardará las cadenas de aminoácidos
for i in range(2):		#2 veces: de ida y complemente de regreso
	ini=dna.find('ATG')	#busca posición de ATG codon de inicio
	while ini!=-1:		#si encontró
		aminos.append('ATG')	#agregar nueva cadena que inicia con 3 bases
		fin=ini+3		#avanza al sig codon
		while dna[fin:fin+3] not in ['TAA','TAG','TGA']:	#mientras no encuentre any cadena de fin
			aminos[-1]+=dna[fin:fin+3]						#agregarlas a la cadena que estamos creando
			fin+=3		#avanza al sig codon
			if fin>len(dna):								#si llegó al fin de la cadena dna
				del aminos[-1]								#eliminar la que se contruía y salir del while que busca fin
				break
		ini=dna.find('ATG',ini+3)							#buscar el inicio de sig cadena de aminos
	
	dna2=''				#crearemos complemento
	for i in dna[::-1]:	#del inverso
		if i=='A':
			dna2+='T'
		elif i=='C':
			dna2+='G'
		elif i=='G':
			dna2+='C'
		elif i=='T':
			dna2+='A'
	dna=dna2			#y volveremos a buscar cadenas de aminos ahora con el complemento

#convertir a proteinas
aminos=list(set(aminos))	#convertir a set elimina los repetidos (y desordena)
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
prots=[]	#lista de proteínas
for cadaminos in aminos:		#para cada cadena de aminoácidos
	prots.append('')			#crear nueva cadena de proteína
	for codon in range(0,len(cadaminos),3):				#por cada tripleta de bases
		prots[-1]+=aminobases[cadaminos[codon:codon+3]]	#agregar su aminoácido
print prots	#imprime lista de proteínas

#guardar resultados
scribo=open('rosalind_answer.txt','w')
for p in prots:
	scribo.write(p+'\n')
scribo.close()
#abrir archivo de resultados
from os import system
system('gedit rosalind_answer.txt')

#TTT F	CTT L	ATT I	GTT V
#TTC F	CTC L	ATC I	GTC V
#TTA L	CTA L	ATA I	GTA V
#TTG L	CTG L	ATG M	GTG V
#TCT S	CCT P	ACT T	GCT A
#TCC S	CCC P	ACC T	GCC A
#TCA S	CCA P	ACA T	GCA A
#TCG S	CCG P	ACG T	GCG A
#TAT Y	CAT H	AAT N	GAT D
#TAC Y	CAC H	AAC N	GAC D
#TAA Stop   CAA Q	AAA K	GAA E
#TAG Stop   CAG Q	AAG K	GAG E
#TGT C	CGT R	AGT S	GGT G
#TGC C	CGC R	AGC S	GGC G
#TGA Stop   CGA R	AGA R	GGA G
#TGG W	CGG R	AGG R	GGG G

#AGCC ATG [TAG]C[TAA]CTCAGGTTAC ATG GGG ATG ACCCCGCGACTTGGAT[TAG]AGTCTCTTTTGGAA[TAA]GCC[TGA] ATG ATCCGAG[TAG]CATCTCAG
#CTGAG ATG CTACTCGGATCATTCAGGCTTATTCCAAAAGAGACTC[TAA]TCCAAGTCGCGGGGTCATCCCC ATG [TAA]CC[TGA]GT[TAG]CTAC ATG GCT
#ATG
#ATG GGG ATG ACC CCG CGA CTT GGA TTA GAG TCT CTT TTG GAA
#ATG ACC CCG CGA CTT GGA TTA GAG TCT CTT TTG GAA
#ATG CTA CTC GGA TCA TTC AGG CTT ATT CCA AAA GAG ACT CTA ATC CAA GTC GCG GGG TCA TCC CCA TGT AAC CTG AGT
#MLLGSFRLIPKETLIQVAGSSPCNLS
