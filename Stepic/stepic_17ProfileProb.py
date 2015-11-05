# ﻿coding=utf8
# Find a Profile most probable k-mer from a string.
# Given a string Text, an integer k, and a 4*k matrix profile.
# output a profile-most probable k-mer in Text
BASES = ('A', 'C', 'G', 'T')

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
	maxProbable = ['',0]
	for ikmer in range(len(Text)-k+1):
		kmer = Text[ikmer:ikmer+k]
		if maxProbable[1] < Probability(kmer,Profile):
			maxProbable = [kmer,Probability(kmer,Profile)]
	return maxProbable

with open('stepic_profileprob2.txt','r') as leo:
	Text = leo.readline().strip()
	k = int(leo.readline().strip())
	RawProfile = []
	for line in range(4):
		line = [float(num) for num in leo.readline().strip().split()]
		RawProfile.append(line)
Profile = [[RawProfile[j][i] for j in range(4)] for i in range(k)]
#print Profile

print ProfileProbable( Text, Profile, k)
