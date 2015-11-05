#hamming distance: Comparar dos cadenas de igual longitud y contar el número de diferencias
leo=open('rosalind_hamm.txt','r')

strand1=leo.readline()
strand2=leo.readline()
hd=0

for i in range(len(strand1)-1):	#lista de 0 a tamaño_cadena
	if strand1[i] != strand2[i]:
		hd+=1

leo.close()
print hd
raw_input()