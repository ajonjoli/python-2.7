# ﻿coding=utf8
# GreedyMotifSearch: Motif Finding Algorithm based on greedy search
#	for every k-mer in first string, select the best k-mer in 2nd string
#	then from those 2 k-mers select the best k-mer in 3rd string and go on till the last string
#	keep the set of k-mers with BestScore
#	Dna: list of strings, k: size of motif, t: number of strings
from os import system
BASES = ('A', 'C', 'G', 'T')

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
		#maxBase = max(col)
		PosMaxBase = col.index(max(col))
		Consensus += BASES[PosMaxBase]
	return Consensus

def Probability (kmer, Profile):
	prob = 1
	for ibase in range(len(kmer)):
		prob *= Profile[ibase][BASES.index(kmer[ibase])]
#		if kmer[ibase] == 'A':
#			prob *= Profile[ibase][0]
#		elif kmer[ibase] == 'C':
#			prob *= Profile[ibase][1]
#		elif kmer[ibase] == 'G':
#			prob *= Profile[ibase][2]
#		elif kmer[ibase] == 'T':
#			prob *= Profile[ibase][3]
	return prob

def ProfileProbable (Text, Profile, k):
	maxProbable = [Text[:k],0]
	for ikmer in range(len(Text)-k+1):
		kmer = Text[ikmer:ikmer+k]
		if maxProbable[1] < Probability(kmer,Profile):
			maxProbable = [kmer,Probability(kmer,Profile)]
	return maxProbable[0]

def Score (Motifs, k):
	Consensus = MakeConsensus(MakeProfile(Motifs, k))
	Score = 0
	for ik in range(k):
		Score += sum(1 for kmer in Motifs if kmer[ik] != Consensus[ik])
	return Score

def GreedyMotifSearch (Dna, k, t):
	BestMotifs = [string[:k] for string in Dna]
	BestScore = k*t	#minScore
	for ikmer in range(len(Dna[0])-k+1):
		Motifs = [Dna[0][ikmer:ikmer+k]]
		for i in range(1,t):
			Profile = MakeProfile(Motifs,k)
			#print Profile
			newMotif = ProfileProbable( Dna[i], Profile, k)
			Motifs.append(newMotif)
		if BestScore > Score(Motifs, k):
			BestMotifs = Motifs
			BestScore = Score(Motifs, k)
	return BestMotifs
			
with open('stepic_greedymotif2.txt','r') as leo:
	k,t = [int(x) for x in leo.readline().strip().split()]
	Dna = []
	for iline in range(t):
		Dna.append( leo.readline().strip() )
#print k, t
#print Dna
Motifs = GreedyMotifSearch( Dna, k, t)

with open('rosalind_answer.txt','w') as scribo:
	for motif in Motifs:
		print motif
		scribo.write(motif+'\n')
system('gedit rosalind_answer.txt')		#y lo escribe
