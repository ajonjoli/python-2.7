#prot: traducir una cadena de mRNA en una cadena de aminoácidos
leo=open('rosalind_prot.txt','r')
mRNA=leo.readline()
protein=''
aminoacidos={
'UUU':'F',	'CUU':'L',	'AUU':'I',	'GUU':'V',
'UUC':'F',	'CUC':'L',	'AUC':'I',	'GUC':'V',
'UUA':'L',	'CUA':'L',	'AUA':'I',	'GUA':'V',
'UUG':'L',	'CUG':'L',	'AUG':'M',	'GUG':'V',
'UCU':'S',	'CCU':'P',	'ACU':'T',	'GCU':'A',
'UCC':'S',	'CCC':'P',	'ACC':'T',	'GCC':'A',
'UCA':'S',	'CCA':'P',	'ACA':'T',	'GCA':'A',
'UCG':'S',	'CCG':'P',	'ACG':'T',	'GCG':'A',
'UAU':'Y',	'CAU':'H',	'AAU':'N',	'GAU':'D',
'UAC':'Y',	'CAC':'H',	'AAC':'N',	'GAC':'D',
'UAA':'X',	'CAA':'Q',	'AAA':'K',	'GAA':'E',
'UAG':'X',	'CAG':'Q',	'AAG':'K',	'GAG':'E',
'UGU':'C',	'CGU':'R',	'AGU':'S',	'GGU':'G',
'UGC':'C',	'CGC':'R',	'AGC':'S',	'GGC':'G',
'UGA':'X',	'CGA':'R',	'AGA':'R',	'GGA':'G',
'UGG':'W',	'CGG':'R',	'AGG':'R',	'GGG':'G'}

for i in range(0,len(mRNA),3):
	amino=mRNA[i:i+3]
	# if amino in ('AUG'):	#al principio porque siempre aparece, es principio de cadena de aminoácidos
		# protein+='M'
	# elif amino in ('GCU','GCC','GCA','GCG'):
		# protein+='A'
	# elif amino in ('UGU','UGC'):
		# protein+='C'
	# elif amino in ('GAU','GAC'):
		# protein+='D'
	# elif amino in ('GAA','GAG'):
		# protein+='E'
	# elif amino in ('UUU','UUC'):
		# protein+='F'
	# elif amino in ('GGU','GGC','GGA','GGG'):
		# protein+='G'
	# elif amino in ('CAU','CAC'):
		# protein+='H'
	# elif amino in ('AUU','AUC','AUA'):
		# protein+='I'
	# elif amino in ('AAA','AAG'):
		# protein+='K'
	# elif amino in ('UUA','UUG','CUU','CUC','CUA','CUG'):
		# protein+='L'
	# elif amino in ('AAU','AAC'):
		# protein+='N'
	# elif amino in ('CCU','CCC','CCA','CCG'):
		# protein+='P'
	# elif amino in ('CAA','CAG'):
		# protein+='Q'
	# elif amino in ('CGU','CGC','CGA','CGG','AGA','AGG'):
		# protein+='R'
	# elif amino in ('UCU','UCC','UCA','UCG','AGU','AGC'):
		# protein+='S'
	# elif amino in ('ACU','ACC','ACA','ACG'):
		# protein+='T'
	# elif amino in ('GUU','GUC','GUA','GUG'):
		# protein+='V'
	# elif amino in ('UGG'):
		# protein+='W'
	# elif amino in ('UAU','UAC'):
		# protein+='Y'
	# elif amino in ('UAA','UAG','UGA'):
		# break
	if amino in ('UAA','UAG','UGA'):
		break
	protein+=aminoacidos[amino]

print protein
raw_input()
savo=open('rosalind_answer.txt','w')
savo.write(protein)
leo.close()
savo.close()

#lista de combinaciones de 3 bases y el aminoácido que forman
# aminoacidos={
# 'UUU':'F',	'CUU':'L',	'AUU':'I',	'GUU':'V',
# 'UUC':'F',	'CUC':'L',	'AUC':'I',	'GUC':'V',
# 'UUA':'L',	'CUA':'L',	'AUA':'I',	'GUA':'V',
# 'UUG':'L',	'CUG':'L',	'AUG':'M',	'GUG':'V',
# 'UCU':'S',	'CCU':'P',	'ACU':'T',	'GCU':'A',
# 'UCC':'S',	'CCC':'P',	'ACC':'T',	'GCC':'A',
# 'UCA':'S',	'CCA':'P',	'ACA':'T',	'GCA':'A',
# 'UCG':'S',	'CCG':'P',	'ACG':'T',	'GCG':'A',
# 'UAU':'Y',	'CAU':'H',	'AAU':'N',	'GAU':'D',
# 'UAC':'Y',	'CAC':'H',	'AAC':'N',	'GAC':'D',
# 'UAA':'X',	'CAA':'Q',	'AAA':'K',	'GAA':'E',
# 'UAG':'X',	'CAG':'Q',	'AAG':'K',	'GAG':'E',
# 'UGU':'C',	'CGU':'R',	'AGU':'S',	'GGU':'G',
# 'UGC':'C',	'CGC':'R',	'AGC':'S',	'GGC':'G',
# 'UGA':'X',	'CGA':'R',	'AGA':'R',	'GGA':'G',
# 'UGG':'W',	'CGG':'R',	'AGG':'R',	'GGG':'G'}
#except BJOUXZ