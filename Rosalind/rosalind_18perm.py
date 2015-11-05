# ﻿coding=utf8
# Enumerating gene orders
# Dado un entero positivo n<=7 devolver el total de permutaciones y una lista de todas las permutaciones posibles

# prueba 3 = entrega 6
# reto 5 = entrega 120
from itertools import permutations

elements=int(raw_input('Número de elementos a ordenar: '))	#pide el número de elementos a ordenar
permutaciones=[0]											#guarda la lista de permutaciones y el contador primero
for permut in permutations([str(i) for i in range(1,elements+1)]):		#itertools.permutations([1,2,3])
	permutaciones[0]+=1
	permutaciones.append(' '.join(permut)+'\n')				#guarda cada permutación en formato del archivo
permutaciones[0]=str(permutaciones[0])+'\n'					#convertir a formato del archivo

scribo=open('rosalind_answer.txt','w')	#guardar en un archivo
scribo.writelines(permutaciones)
scribo.close()
from os import system
system('gedit rosalind_answer.txt')		#y lo escribe
