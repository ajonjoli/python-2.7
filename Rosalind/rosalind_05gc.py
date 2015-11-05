#gc content: Encuentra la cadena de adn con mayor porcentaje de C y G
leo=open('rosalind_gc.txt','r')

dna=0
gc=0
gcmax=0.0
f=leo.read(1)

while f!='>':
	f=leo.read(1)
while f!='':	#EOF
	label=leo.read(13)	#etiqeta con formato FASTA: Rosalind_xxxx con 0000<=xxxx<=9999
	f=leo.read(1)
	while f not in ('>',''):	#f!='>' and f!='':
		if f in ('A','T'):	#if f=='A' or f=='T':
			dna+=1
		if f in ('C','G'):	#if f=='C' or f=='G':
			dna+=1
			gc+=1
		f=leo.read(1)
	gc100=(gc*100.0)/dna	#porcentaje de GC
	#print label,gc100
	#raw_input()
	if gc100>gcmax:	#burbuja al mayor
		gcmax=gc100
		labelmax=label
	dna=0	#reinician contadores
	gc=0

savo=open('rosalind_answer.txt','w')
savo.write(labelmax+'\n'+str(gcmax))
leo.close()
savo.close()