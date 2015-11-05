#Grafos sobrepuestos: dado un conjunto de nodos, se enlazan mediante aristas
#cada cadena con subcadena final de k elementos igual a la subcadena inicial de k elementos de otra cadena
#Se muestra los enlaces mediante una lista de adyacencia (x,y) (x,z) (a,b) (z,a)
#k=3
leo=open('rosalind_grph.txt','r')
vertix=[]
dna=''
temp=leo.readline().strip()	#lee mientras no se sepa si es etiqeta FASTA o cadena adn
while temp!='':
	if temp[0]=='>':	#si etiqeta FASTA
		if dna!='':
			vertix.append([fasta,dna])	#guarda en lista de vértices
		fasta=temp[1:]
		dna=leo.readline().strip()	#empieza nueva cadena adn
	else:
		dna+=temp	#concatena a la nueva parte
	temp=leo.readline().strip()	#vuelve a leer sin saber
vertix.append([fasta,dna])	#guarda el último
leo.close()

aristas=[]	#lista de adyacencia
for fas1,dn1 in vertix:
	for fas2,dn2 in vertix:	#n^2
		if fas1!=fas2 and dn1[-3:]==dn2[:3]:	#si son distintos y el sufijo del 1 es el prefijo del 2
			aristas.append([fas1,fas2])			#guardar en lista de adyacencia

savo=open('rosalind_answer.txt','w')
for a,b in aristas:
	print a,b
	savo.write(a+' '+b+'\n')	#presentación de resultados
savo.close()
raw_input()