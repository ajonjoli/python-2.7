# ﻿coding=utf8
#Functions that work using Dynamic Programming.
#	bottom-up technique that solves subproblems
#	in order to solve uper level subproblems using the lower level subproblems solutions
#	so that the final problem is solved using the subproblems solutions

def MinNumberCoins (S, coins):
	minim = [1000]* (S+1)	#very large number
	minim[0] = 0			#final recursion, base
	values = [[]]* (S+1)	#values of the coins needed

	for i in range(1,S+1):
		for j in range(len(coins)):
			if coins[j] <= i and minim[ i-coins[j] ]+1 < minim[i]:
			# if this coin values equal or less than i and
			# the coins needed before this coin + this 1 coin is less than the minimum found so far
				minim[i] = minim[i-coins[j]]+1	#change minimum found
				values[i] = values[ i-coins[j] ]+[ coins[j] ]
	#print minim,'\n',values
	return minim[S],values[S]

S = 11	#number to reach
coins = (1, 3, 5)	#values of coins
MinCoins,Values = MinNumberCoins(S, coins)
print MinCoins,Values
	
def LongestSequence (sequence):
	k = len(sequence)
	#sizes = [0]* k	#largest number
	seqs = [[]]* k	#sequences found

	for i in range(k):
		#sizes[i] = 1
		seqs[i] = [sequence[i]]
		for j in range(i):
			if sequence[j] < sequence[i] and len(seqs[j])+1 > len(seqs[i]):
				#sizes[i] = sizes[j]+1	#change minimum found
				seqs[i] = seqs[j]+[sequence[i]]
	print seqs#,max(seqs, key=len)
	return max(seqs, key=len)

sequence = (5, 3, 4, 8, 6, 7)	#sequence to use
LongSeq = LongestSequence(sequence)
print LongSeq	#final result
print LongestSequence((5,2,8,6,3,6,9,7))

def LongestCommonSequence (seq1, seq2):
	k1 = len(seq1)
	k2 = len(seq2)
	#sizes = [0]* k	#largest number
	subseqs = [[]]* k1	#sequences found

	for i in range(k1):
		if seq1[i] in seq2:
			#sizes[i] = 1
			subseqs[i] = [seq1[i]]
			for j in range(i):
				#if i was found after j and length thanks to j is better than current length of i
				if seq2.find(seq1[j]) < seq2.find(seq1[i],seq2.find(seq1[j])) and len(subseqs[j])+1 > len(subseqs[i]):
					#sizes[i] = sizes[j]+1	#change minimum found
					subseqs[i] = subseqs[j]+[seq1[i]]
	print subseqs#,max(seqs, key=len)
	return max(subseqs, key=len)

seq1 = 'AXBCDEFG'
seq2 = 'CXXDXXG'
print 'LongestSequence'
print LongestCommonSequence(seq1, seq2)
#if len(seq1)<=len(seq2) else LongestCommonSequence(seq2, seq1)

def MinSteps2one (n):
	steps = [1000]* n	#number of steps per number in 1...n
	steps[0] = 0	#index = 0, number = 1

	for i in range(1,n):
		numb = i+1		
#		for j in (i-1,(numb/2)-1 if numb%2==0 else i-1, (numb/3)-1 if numb%3==0 else i-1):
#			if steps[j]+1 < steps[i]:
#				steps[i] = steps[j]+1
		steps[i] = steps[i-1]+1
		if numb%2 == 0:
			steps[i] = min( steps[i],steps[(numb/2)-1]+1 )
		elif numb%3 == 0:
			steps[i] = min( steps[i],steps[(numb/3)-1]+1 )
	print steps
	return steps[-1]

n=13
#print MinSteps2one(n),'steps to number',n

def Fibonacci (N):
	if N == 0:
		return 0
	elif N == 1:
		return 1
	
	PrevFibs = [1,1]
	for index in range(N-1):	#only times to repeat
		NewFib = sum(PrevFibs)
		PrevFibs[index%2] = NewFib	#changes the oldest one
		#print PrevFibs
	return NewFib

for i in range(6+1):
	print i,'=>',Fibonacci(i)
	
def MostApples (Land):
	rows = len(Land)
	cols = len(Land[0])
	#QuantApples = [[0]*cols for i in range(rows)]
	path = []
	#print cols,rows
	
	for i in range(rows):
		for j in range(cols):
			Land[i][j] = Land[i][j] + max(Land[i-1][j] if i>0 else 0, Land[i][j-1] if j>0 else 0)
	#print Land
	
	i,j=rows-1,cols-1
	while i>0 or j>0:
		path.append(Land[i][j])
		#i,j = i-1,j if Land[i-1][j] >= Land[i][j-1] else i,j-1
		if j-1 < 0:
			i -= 1
		elif i-1 < 0:
			j -= 1
		elif Land[i-1][j] >= Land[i][j-1]:
			i -= 1
		else:
			j -= 1
		
	path.reverse()
	print path
	return Land[-1][-1]

Land = [ [1,10,4,3,6], [7,5,3,9,2], [2,2,2,2,1], [7,36,5,4,1] ]
print MostApples (Land)

def Knapsack (Capacity, Items):
	n = len(Items)
	capacities = [[0]* (Capacity+1) for x in range(n+1)]
	#print capacities,len(capacities),len(capacities[0])
	
	for i in range(1,n+1):
		for w in range(1,Capacity+1):
			if Items[i-1][0] > w:
				capacities[i][w] = capacities[i-1][w]
			else:
				capacities[i][w] = max( capacities[i-1][w], capacities[i-1][w-Items[i-1][0]]+Items[i-1][1] )
	#print capacities
	return capacities[-1][-1]

Capacity = 11
Items = ( (1,1), (2,6), (5,18), (6,22), (7,28) )	#weight,value
print Knapsack(Capacity,Items)

#PABEL PAAAAAAAAABEEEEEEEEEELLL
def EditDistance (word1, word2, mismatch=1, gap=1):
	k1, k2 = len(word1), len(word2)
	EditMatrix = [[[0.0,''] for x in range(k2+1)] for y in range(k1+1)]
	
	#fill the first row and col
	for i in range(k1+1):
		EditMatrix[i][0] = [i*mismatch, word1[:i] ]
	for j in range(k2+1):
		EditMatrix[0][j] = [j*mismatch, word2[:j] ]
	#print EditMatrix
	
	for i in range(1,k1+1):
		for j in range(1,k2+1):
			diff = 0 if word1[i-1] == word2[j-1] else mismatch 	#match = 0, mismatch = 1
			#print EditMatrix[i-1][j], EditMatrix[i][j-1], EditMatrix[i-1][j-1]
			EditMatrix[i][j] = min( [EditMatrix[i-1][j][0]+gap, EditMatrix[i-1][j][1]+'-'],\
									[EditMatrix[i][j-1][0]+gap, EditMatrix[i][j-1][1]+'-'],\
									[EditMatrix[i-1][j-1][0]+diff, \
									EditMatrix[i-1][j-1][1]+word1[i-1] if diff==0 else EditMatrix[i-1][j-1][1]+'*'] )
	#print EditMatrix
	return EditMatrix[-1][-1]

word1 = 'EXPONENTIAL'
word2 = 'POLYNOMIAL'
word1 = 'ACAGTA'
word2 = 'GCAGGTA'
print word1, word2 
print EditDistance(word1,word2, gap=3)
#print EditDistance('snowy','sunny')
#print EditDistance('ACACACTA','AGCACACA')

def CreateGraph (Edges):
	Graph = {} #node:{} for node in range(NumNodes)}	#dictionary of distionaries
	
	for edge in Edges:	#list of lists
		if edge[0] not in Graph.keys():
			Graph[edge[0]] = {}
		if edge[1] not in Graph.keys():
			Graph[edge[1]] = {}
		Graph[edge[0]] [edge[1]] = edge[2]
		#Graph[edge[1]] ['parents'].append( edge[0] )
	print Graph
	return Graph

def FindAllParents (Graph, child):
	return [node for node in Graph.keys() if child in Graph[node].keys()]
#	AllParents = []
#	for node in Graph.keys():
#		if child in Graph[node].keys():
#			AllParents.append(node)
#	return AllParents

def BreadthFirstSort (Graph, Source):
	#Topological Sorting
	SortedNodes = []
	children = []
	Parents = [Source]
	while len(Parents) > 0:
		parent = Parents.pop(0)
		SortedNodes.append(parent)
		for child in Graph[parent].keys():
			if child not in SortedNodes+Parents+children:
				children.append(child)
		for child in children:
			if set( FindAllParents(Graph,child) ).issubset(Parents+SortedNodes):
				children.remove(child)
				Parents.append(child)
	print SortedNodes
	return SortedNodes

def ShortestPath (Graph, Source, Sink):
	if Source not in Graph.keys() or Sink not in Graph.keys():
		return None

	#distances = [1000]* len(Graph.keys())
	#distances[0] = 0
	#steps = [[]]* NumNodes
	#steps[0] = [0]	
	distances = {node:1000 for node in Graph.keys() }
	distances[Source] = 0
	
	for node in BreadthFirstSort(Graph,Source)[1:]:
		distances[node] = min ( distances[parent]+Graph[parent][node] for parent in FindAllParents(Graph,node) )
	print distances
	return distances[Sink]

#NumNodes = 6
Edges = (('S','A',1),('S','C',2),('C','A',4),('A','B',6),('C','D',3),('B','D',1),('B','E',2),('D','E',1))	#Edges: ordered x1, x2, weight
Source, Sink = 'S', 'D'
print ShortestPath( CreateGraph (Edges), Source, Sink )

