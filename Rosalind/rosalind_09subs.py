#subs: encontrar las localizaciones de una subcadena t en la cadena s
#encuentra incluso cuando una aparición contiene al inicio de la sig aparición buscar ATAT en ATATATATATAT
leo=open('rosalind_subs.txt','r')
dna=leo.readline()
dna=dna.replace('\n','')
sub=leo.readline()
sub=sub.replace('\n','')
#print dna+'++'+sub+'++'

founds=[]
index=0

while index<len(dna):
	index=dna.find(sub,index)
	if index==-1:
		break
	founds.append(index+1)
	index+=1

#for i in founds:
#	print i,
#	raw_input()

savo=open('rosalind_answer.txt','w')
for i in founds:
	savo.write(str(i)+' ')
leo.close()
savo.close()