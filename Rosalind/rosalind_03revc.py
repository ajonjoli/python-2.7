intro=open('rosalind_revc.txt','r')
gardo=open('rosalind_answer.txt','w')
strand=intro.read(1)
complement=''
while strand!='':
	if strand=='A':
		strand='T'
	elif strand=='C':
		strand='G'
	elif strand=='G':
		strand='C'
	elif strand=='T':
		strand='A'
	if strand!='\n':
		complement=strand+complement
	strand=intro.read(1)
gardo.write(complement)
intro.close()
gardo.close()