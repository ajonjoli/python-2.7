# ﻿coding=utf8
# RandomizedMotifSearch: Motif Finding Algorithm based on randomized algorithms
#	randomly select a k-mer per string, creates a profile
#	based on that profile selects the best matching k-mer per each string
#	based on those new k-mer creates a new profile and calculate the Score
#	exit from cycle when the Score can't be better
#	Outside this method can be called many times to get an even better Score
#	Dna: list of strings, k: size of motif, t: number of strings
from random import randint	#a<=x<=b
from os import system
BASES = ('A','C','G','T')

def MakeProfile (Motifs, k):
	#[A C G T][A C G T][A C G T]
	Profile = [ [1.0]*4 for x in range(k) ]
	for kmer in Motifs:
		for ik in range(k):
			Base = kmer[ik]
			PosBase = BASES.index(Base)
			Profile[ik][PosBase] += 1
	return [[n/len(Motifs)+4 for n in row] for row in Profile]

def MakeConsensus (Profile):
	Consensus = ''
	for col in Profile:
		PosMaxBase = col.index(max(col))
		Consensus += BASES[PosMaxBase]
	return Consensus

def Probability (kmer, Profile):
	prob = 1
	for ibase in range(len(kmer)):
		prob *= Profile[ibase][BASES.index(kmer[ibase])]
	return prob

def ProfileProbable (Text, Profile, k):
	maxProbable = [Text[:k],0]
	for ikmer in range(len(Text)-k+1):
		kmer = Text[ikmer:ikmer+k]
		if maxProbable[1] < Probability(kmer,Profile):
			maxProbable = [kmer,Probability(kmer,Profile)]
	return maxProbable[0]

def SearchMotifs (Profile, Dna, k):
	Motifs = []
	for string in Dna:
		newMotif = ProfileProbable( string, Profile, k)
		Motifs.append(newMotif)
	return Motifs

def Score (Motifs, k):
	Consensus = MakeConsensus(MakeProfile(Motifs, k))
	Score = 0
	for ik in range(k):
		Score += sum(1 for kmer in Motifs if kmer[ik] != Consensus[ik])
	return Score

def RandomizedMotifSearch (Dna, k, t):
	SizeString = len(Dna[0])
	#print SizeString,Dna[0][:k],Dna[0][SizeString-k:]
	BestMotifs = []
	BestScore = k*t	#minScore
	for it in range(t):
		RandInt = randint(0,SizeString-k)
		#print RandInt,Dna[it][RandInt:RandInt+k]
		BestMotifs.append( Dna[it][RandInt:RandInt+k] )
	#print BestMotifs
	while True:	#too dangerous
		Profile = MakeProfile(BestMotifs,k)
		Motifs = SearchMotifs(Profile, Dna, k)
		if BestScore > Score(Motifs, k):
			BestMotifs = Motifs
			BestScore = Score(Motifs, k)
		else:
			return BestScore,BestMotifs

with open('stepic_randomizedmotif2.txt','r') as leo:
	k,t = [int(x) for x in leo.readline().strip().split()]
	Dna = []
	for iline in range(t):
		Dna.append( leo.readline().strip() )
print k, t
#print Dna

BestScore = k*t
for i in range(1000):
	NewScore,NewMotifs = RandomizedMotifSearch (Dna, k, t)
	if BestScore > NewScore:
		BestScore = NewScore
		BestMotifs = NewMotifs

with open('rosalind_answer.txt','w') as scribo:
	for motif in BestMotifs:
		print motif
		scribo.write(motif+'\n')
system('gedit rosalind_answer.txt')		#y lo escribe
