repro=0		#pares capaces de tener crías
bebes=0		#pares de crias en el mes
adoles=0	#temporal
n=0
k=0
print 'Fibonacci de conejos'
n=raw_input("Dame n <=40: ")
k=raw_input("Dame k <=5: ")
#k es el número de parejas de bebés que produce cada pareja
#m es el número de meses después que se cuentan los conejos
for i in range(int(n)):
	if i==0:
		bebes=1	#los primeros no pueden tener hijos
	elif i==1:
		bebes=0	#ya no son bebés
		repro=1	#ahora pueden tener crías
	else:
		adoles=bebes	#los bebes que habían crecen
		bebes=repro*int(k)	#todas las parejas reproductoras tienen crías
		repro=adoles+repro	#los nuevos reproductores + los anteriores
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