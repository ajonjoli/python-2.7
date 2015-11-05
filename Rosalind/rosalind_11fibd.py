#Mortal Fibonacci Rabbits: como en fib04.py excepto que cada mes nacen de cada pareja 1 pareja (1macho,1hembra) y los conejos mueren a los m meses
repro=0		#pares capaces de tener crías
bebes=0		#pares de crias en el mes
adoles=0	#temporal
from collections import deque	#importar colas
moriran=deque()	#cola vacía
n=0	#n es el número de meses después que se cuentan los conejos
k=1	#k es el número de parejas de bebés que produce cada pareja
m=0	#m es el número de meses después de que nacen que mueren los conejos
print 'Fibonacci de conejos'
n=int(raw_input('Dame n <=100: '))
m=int(raw_input('Dame m <=20: '))

for i in range(n):
	if i==0:
		bebes=1	#los primeros no pueden tener hijos
	elif i==1:
		bebes=0		#ya no son bebés
		repro=1		#a la sig podrán reproducir
	else:
		adoles=bebes	#los bebes que habían crecen
		bebes=repro	#todas las parejas reproductoras tienen crías (1 pareja)
		repro=adoles+repro	#los nuevos reproductores + los anteriores
	
	moriran.append(bebes)	#las crías que acaban de nacer entran a la cola del destino
	if i>=m:	#si ya es hora que empiecen a morir
		if repro>0:	#y hay adultos
			repro-=moriran.popleft()	#salen de los reproductores
		else:			#morirán los bebés pues no hay de otro tipo con vida
			bebes-=moriran.popleft()
print repro+bebes
raw_input()
#1: en mes=0, 1 par
#2: en mes=1, 1 par reproductor
#3: en any mes, cada par reproductor mates
#4: en any mes +1, cada par reproductor produce un 1 par
#5: rabitts never die or stop
# mes=0 par=1h, mes=1 par=1r, mes=2 par=1r+1h=2, mes=3 par=1r+1r+1h=3, mes=4 par=1r+1r+1r+1h+1h=5
# mes=5 par=1r+1r+1r+2r+3h=8, mes=6 par=5r+3r+5h=13
# 1,1,2,3,5,8,13,