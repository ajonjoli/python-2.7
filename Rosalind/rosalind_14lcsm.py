#Finding shared motif: dado un conjunto de cadenas de ADN en formato FASTA, encontrar la subcadena en común más larga,
#si hay varias, encontrar solo una

leo=open('rosalind_lcsm.txt','r')
dnas=[]
dna=''
temp=leo.readline().strip()	#lee mientras no se sepa si es etiqeta FASTA o cadena adn
while temp!='':
	if temp[0]=='>':	#si etiqeta FASTA
		if dna!='':			#y ya creó una cadena dna
			dnas.append(dna)	#guarda en lista de cadenas
		dna=leo.readline().strip()		#empieza nueva cadena adn
	else:
		dna+=temp	#concatena la nueva parte
	temp=leo.readline().strip()	#vuelve a leer sin saber
dnas.append(dna)	#guarda el último
leo.close()

dnas.sort(key=len)	#así compara primero los más cortos, con menos subcadenas en común
dnamin=dnas[0]	#cadena más corta
#print dnas,dnamin

subdna=''	#guardará subcadena común
for sub in range(len(dnamin)):	#recorre la posición inicial de subcadenas
	inner=False			#indicará si la subcadena está en todas las cadenas
	dest=len(dnamin)	#inicia con subcadenas más largas y las acorta
	while not inner and dest>=1:	#hasta subcadena de 1 char
		#print dnamin[sub:dest]
		for d in dnas[1:]:	#buscará en todas las demás cadenas
			if dnamin[sub:dest] not in d:	#si no está, levanta bandera...
				#print 'not in',d,sub,dest
				inner=False
				dest-=1	#disminuye un elemento
				break	#y sale del for(todas demás cadenas)
			inner=True		#lo encontró en cada cadena
		if len(subdna)>len(dnamin[sub:dest]) and subdna!='':	#si ya es menor que la subcadena común no seguir buscando
			break	#y sale del while not inner
	if inner and len(subdna)<len(dnamin[sub:dest]):	#lo encontró y es mayor
		#print 'found:',subdna,dnamin[sub:dest],sub,dest
		subdna=dnamin[sub:dest]	#lo guarda en subcadena común

#presentación de resultados
print 'substring:',subdna
savo=open('rosalind_answer.txt','w')
savo.write(subdna)
savo.close()
#raw_input()
