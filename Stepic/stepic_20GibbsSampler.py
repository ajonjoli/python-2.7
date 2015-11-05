# ﻿coding=utf8
# GibbsSampler: Motif Finding Algorithm based on optimized randomized algorithms
#	Dna: list of strings, k: size of motif, t: number of strings, N: number of iterations (k-mer in 1 string changes per iteration)
#	First randomly select a k-mer per string and gets their score
#	remove one k-mer and create profile from the others motifs
#	from the k-mer removed, go to its string, calculate probability of all its k-mers
#	use their probabilties as probability distribution to take randomly one k-mer
#	insert the new k-mer in the list of motifs and get their score
#	if the score is better than the best one, replace it
#	iterate N times and return the motifs with the best score till that moment
#	Outside this method can be called many times to get an even better Score
from random import randint	#a<=x<=b
from numpy import random as nprandom
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
	return [[n/(len(Motifs)+4) for n in row] for row in Profile]

def MakeConsensus (Motifs, k):
	Consensus = ''
	for col in MakeProfile(Motifs,k):
		PosMaxBase = col.index(max(col))
		Consensus += BASES[PosMaxBase]
	return Consensus

def Probability (kmer, Profile):
	prob = 1
	for ibase in range(len(kmer)):
		prob *= Profile[ibase][ BASES.index( kmer[ibase] ) ]
	return prob

def WeightedRandom (Weights):
	Weights = [w/sum(Weights) for w in Weights]
	return nprandom.choice( len(Weights),p=Weights )

def ProfileRandom (Text, Profile, k):
	Weights = []
	for ikmer in range(len(Text)-k+1):
		Weights.append( Probability(Text[ikmer:ikmer+k],Profile) )
	#debug = [x for x,y in enumerate(Weights) if y==max(Weights)]
	#print debug
	ikmer = WeightedRandom( Weights )
	#print [ikmer],Text[ikmer:ikmer+k], ikmer in debug
	return Text[ikmer:ikmer+k]

def Score (Motifs, k):
	Consensus = MakeConsensus(Motifs, k)
	Score = sum( 1 for ik in range(k) for kmer in Motifs if kmer[ik] != Consensus[ik] )
	return Score

def GibbsSampler (Dna, k, t, N):
	SizeString = len(Dna[0])
	Motifs = []
	for it in range(t):
		RandInt = randint(0,SizeString-k)
		Motifs.append( Dna[it][RandInt:RandInt+k] )
	BestMotifs = list(Motifs)
	BestScore = Score(BestMotifs, k)	#minScore
	for n in range(N):
		iString = randint(0,t-1)
		Motifs.pop( iString )
		Profile = MakeProfile(Motifs,k)
		NewMotif = ProfileRandom( Dna[iString], Profile, k )
		Motifs = Motifs[:iString]+[NewMotif]+Motifs[iString:]
		if BestScore > Score(Motifs, k):
			BestMotifs = list(Motifs)
			BestScore = Score(Motifs, k)
	return BestScore,BestMotifs

with open('stepic_gibbssampler.txt','r') as leo:
	k,t,N = [int(x) for x in leo.readline().strip().split()]
	Dna = []
	for iline in range(t):
		Dna.append( leo.readline().strip() )
print k, t, N
#print Dna

BestScore = k*t
for i in range(100):
	NewScore,NewMotifs = GibbsSampler (Dna, k, t, N)
	if BestScore > NewScore:
		BestScore = NewScore
		BestMotifs = NewMotifs
#	print 'New'
#	for motif in BestMotifs:
#		print motif

#BestMotifs = GibbsSampler (Dna, k, t, N)
print 'Final Result',BestScore
for motif in BestMotifs:
	print motif

with open('rosalind_answer.txt','w') as scribo:
	for motif in BestMotifs:
		scribo.write(motif+'\n')
system('gedit rosalind_answer.txt')		#y lo escribe
