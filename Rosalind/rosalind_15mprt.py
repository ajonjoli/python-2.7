# -*- coding: utf-8 -*-
# Finding a protein motif: de una lista de proteinas, buscar un patron determinado en cada una
# y mostrar solo las proteinas en que aparece dicho patrón y los lugares en que aparece
# El patrón es ﻿N-glycosylation: N{P}[ST]{P} = N, cualqiera excepto P, una S o T y cualqiera excepto P.
# Se consultan las secuencias de las proteinas de http://www.uniprot.org/uniprot/uniprot_id.fasta donde en uniprot_id va el nombre de la proteina
import urllib2,re	#importa las librerías para manejo de URLs y expresiones regulares

#lee archivo de proteínas
leo=open('rosalind_mprt.txt','r')
prots=[]	#lista de proteinas donde buscar
tmp=leo.readline().strip()
while tmp!='':		#hasta encontrar línea vacía
	prots.append(tmp)
	tmp=leo.readline().strip()	#vuelve a leer
leo.close()
print prots

#reg=re.compile('N[^P][ST][^P]')
reg=re.compile('(?=(N[^P][ST][^P]))')	#compila expresión regular de N-glycosylation que usarán todas las búsquedas
resultado=[]	#lista de líneas para el archivo de resultados
for p in prots:		#para cada proteína
	#consulta de URL
	url='http://www.uniprot.org/uniprot/'+p+'.fasta'	#crea cadena de dirección
	print url
	consulta=urllib2.urlopen(url)	#abre URL
	consulta.readline()				#tira 1a línea de etiqueta
	sequence=consulta.read().replace('\n','')	#guarda el resto quitando los cambios de línea

	#busca patrón
	found=reg.finditer(sequence)	#un iterador sobre las subcadenas encontradas
	resultado.append(p+'\n')		#guarda la proteina buscada
	resultado.append('')
	for f in found:					#para cada subcadena encontrada
		print f.start()+1,			#guarda la posición de inicio, en archivo inicia con 1, en cadena inicia con 0
		resultado[-1]+=str(f.start()+1)+' '	#y también en resultado
	if resultado[-1]:				#si el iterador recorrió algo, pasa al sig
		print
		resultado[-1]=resultado[-1][:-1]+'\n'
	else:							#si no, borra la proteína donde no encontró nada
		resultado[-2:]=[]			#donde iba la proteína y donde no fueron sus posiciones de subcadenas
	
	consulta.close()

#presentación de resultados
savo=open('rosalind_answer.txt','w')
savo.writelines(resultado)
savo.close()
