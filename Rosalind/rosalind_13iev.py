#Calculating Expected Offspring: dados 6 enteros que representan el número de parejas de cada par genotipo
#1:AA-AA, 2:AA-Aa, 3:AA-aa, 4:Aa-Aa, 5:Aa-aa, 6:aa-aa
#calcular el promedio del fenotipo dominante en la generación resultante,
#se asume qe cada pareja tuvo 1 par

padres=raw_input('Las 6 parejas de cada tipo son: ').split()	#pide los pares de cada pareja: a1 a2 a3 a4 a5 a6
padres=[float(p) for p in padres[:6]]	#convierte a flotante los primeros 6
#print padres

prob=[1.0,1.0,1.0,0.75,0.5,0.0]	#tabla de probabilidad de que sea dominante correspondiente a cada par de padres
savg=0.0	#acumula el promedio
for p in range(len(padres)):
	savg+=padres[p]*prob[p]*2	#formula de cada probablidad, cuántos_c/u*prob(c/u)*2_hijos_resultantes
print savg
raw_input()