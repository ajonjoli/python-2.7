intro=open('rosalind_rna.txt','r')
strand=intro.read(1)
gardo=open('rosalind_rna_answer.txt','w')
while strand!='':
	if strand=='T':
		strand='U'
	gardo.write(strand)
	strand=intro.read(1)
intro.close()
gardo.close()