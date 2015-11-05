#consensus and profile: Buscar el más cercano ancestro común
#recibe n cadenas de adn con su etiqeta FASTA, y devuelve su:
#profile matrix: tabla que indica cuántos hay de cada base en cada posición
#consensus string: cadena con las bases que más aparecen en cada posición
#	si alguna posición tiene más de una base mayor se hacen varias cadenas con cada uno de estas bases mayores
#	este programa solo encuentra una de esas consensus string
leo=open('rosalind_cons.txt','r')
matriz=[]	#guarda las cadenas adn a usar
show=[]		#guarda lo que se meterá al archivo resultado
bases={0:'A',1:'C',2:'G',3:'T'}	#relaciona cada base con un número

fasta=leo.readline()	#lee la etiqeta
fasta=fasta.replace('\n','')
adn=''
while fasta!='':
	if fasta[0]=='>':	#si es una etiqeta FASTA
		if adn!='':
			matriz.append(adn)	#meter a la matriz de listas
		adn=leo.readline()	#lee principio de cadena adn
	else:
		adn+=fasta	#no era una etiqeta FASTA sino el resto de la cadena adn
	adn=adn.replace('\n','')
	fasta=leo.readline()	#lee sig línea y cree es FASTA
	fasta=fasta.replace('\n','')
matriz.append(adn)	#guarda la última cadena adn

leo.close()
cont=range(len(matriz))		#total de cadenas adn
tam=range(len(matriz[0]))	#tamaño de cada adn
#print len(cont),len(tam)

mprofile=[[0]*4 for i in tam]	#declara con 0s
for i in tam:
	for j in cont:
		chk=matriz[j][i]
		for k in range(4):	#recorre bases, eqivale a los ifs debajo
			if chk==bases[k]:
				mprofile[i][k]+=1
		#if chk=='A':
			# mprofile[i][0]+=1
		# elif chk=='C':
			# mprofile[i][1]+=1
		# elif chk=='G':
			# mprofile[i][2]+=1
		# elif chk=='T':
			# mprofile[i][3]+=1
#print mprofile

consensus=[]
for i in tam:
	consensus.append(max(mprofile[i]))	#mete a lista el mayor de cada sublista
	for j in range(4):
		if consensus[i]==mprofile[i][j]:	#recorre para buscar la base de ese contado mayor
			consensus[i]=bases[j]
			break
show.append(''.join(consensus)+'\n')

#Producto cartesiano: encuentra todas las combinaciones de bases máximas, no usar cuando muchas posiciones tienen más de 1 base máxima
#ej. A C G TA G produce: ACGTG Y ACGAG
# maximos=[]
# consensus=['']*len(tam)
# for i in tam:
	# maximos.append(max(mprofile[i]))
	# for j in range(4):
		# if maximos[i]==mprofile[i][j]:
			# consensus[i]+=bases[j]
# show.append(''.join(consensus)+'\n')

# from itertools import product
# for i in product(*consensus):	#producto cartesiano
	# show.append(''.join(i)+'\n')

for i in range(4):	#acomoda profile matrix al formato requerido
	show.append(bases[i]+':')	#A:
	for j in tam:
		show[-1]+=' '+str(mprofile[j][i])	#4 6 2 0 1
	show[-1]+='\n'	#con [enter]
show[-1]=show[-1].replace('\n','')	#excepto último

#print show
print ''.join(show)	#lo que entrará al archivo
savo=open('rosalind_answer.txt','w')
savo.writelines(show)	#escribe los resultados en archivo
savo.close()
raw_input()