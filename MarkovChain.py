# ﻿coding=utf8
import numpy as np
from math import fsum

class MarkovChain:
	"""Class that build a Markov chain to use"""
	# attributes of class

	def __init__ (self, Edges, Aperiodic=True, SingleRecurrent=True):
		self.Edges = Edges 	#attribute of object
		self.Aperiodic = Aperiodic	#Aperiodic, SingleRecurrent
		self.SingleRecurrent = SingleRecurrent
		self.Graph = self.CreateGraph(Edges)
		if self.Graph:
			self.Vertices = tuple(self.Graph.keys())
			self.NumVertex = len(self.Vertices)
			print [x for x in self.Vertices],type(self.Vertices)
			self.TPM = self.CreateTPM()

	# def getNumNodes (self):
	# 	return self.NumNodes

	def CreateGraph (self, Edges):
		Graph = {} #node:{} for node in range(NumNodes)}	#dictionary of distionaries
		
		for edge in Edges:	#list of lists
			if edge[0] not in Graph.keys():
				Graph[edge[0]] = {}
			if edge[1] not in Graph.keys():
				Graph[edge[1]] = {}
			Graph[edge[0]] [edge[1]] = edge[2]
		#all([ True if sum(y)>=5 else False for y in [x for x in a.values()] ])
		#len([True for y in [x for x in a.values()] if sum(y)>=5]) == len(a.keys())
		#check the edges coming from each node sum to 1
		uncomplete = [node for node,ds in [(node,ds) for node,ds in Graph.items()] if fsum(ds.values()) <> 1.0]
		if uncomplete != []:
			print 'Cant create a Markov Chain, edges of nodes',uncomplete,'dont sum to 1'
			print uncomplete,[fsum(Graph[node].values()) for node in uncomplete]
			return
		else:
			#print Graph
			return Graph

	def Prob (self, i, j):
		return self.Graph[i][j]

	def pathProb (self, *nodes):	#calculate the probability of a path of nodes
		if not self.Graph:
			return 0
		Probability = 1
		for inode in range(len(nodes)-1):
			if nodes[inode+1] in self.Graph[ nodes[inode] ].keys():
				Probability *= self.Graph[ nodes[inode] ][ nodes[inode+1] ]
			else:
				return 0
		return Probability

	def CreateTPM (self):	#TransitionProbabilityMatrix
		#print self.Vertices
		TPM = [[0.0]* len(self.Vertices) for v in self.Vertices]
		for iNode,NodeSource in enumerate(self.Vertices):
			for jNode,NodeDestiny in enumerate(self.Vertices):
				if NodeDestiny in self.Graph[NodeSource].keys():
					TPM[iNode][jNode] = self.Graph[NodeSource][NodeDestiny]
		print TPM
		return TPM

	def GetTPM (self,i,j):
		return self.TPM[ self.Vertices.index(i) ][ self.Vertices.index(j) ]

	def ChapmanKolmogorov (self, i, j, n):
		#r_ij(n) = sum(k=1..m)r_ik(n-1)*p_kj if n>1
		#r_ij(1) = p_ij
		if not self.Graph:
			return 0
		# if n == 1:	return self.GetTPM(i,j)
		#declaring the two matrices to save data. Transition Probability Matrices
		#TPMs =	np.array([ self.TPM, [[0.0]* len(self.Vertices) for v in self.Vertices] ])
		TPMs = np.array([ [[0.0]* len(self.Vertices) for v in self.Vertices], self.TPM ])

		for x in range(1,n):	#going up from 2 to n
			TPMs[(x-1)%2] = np.dot( TPMs[x%2], TPMs[x%2] )
		print TPMs
		#return TPMs[(n-1)%2][ self.Vertices.index(i) ][ self.Vertices.index(j) ]
		return TPMs[n%2][ self.Vertices.index(i) ][ self.Vertices.index(j) ]

	def StationaryDistribution (self):
		#it requieres being single recurrent and aperiodic
		if not self.Aperiodic or not self.SingleRecurrent or not self.Graph:
			return 0
		InnerMatrix = np.array(self.TPM) - np.identity(self.NumVertex)	#im=TPM-I
		InnerMatrix = np.concatenate(( np.transpose(InnerMatrix), np.ones((1,self.NumVertex)) ))	#im= im^T + [[1,1,..,1]]
		InnerVector = np.array( [0.0]*self.NumVertex + [1.0] )
		Solutions = np.linalg.lstsq(InnerMatrix,InnerVector)[0]
		print InnerMatrix,InnerVector,Solutions
		return {self.Vertices[vertex]:Solutions[vertex] for vertex in range(self.NumVertex)}

#Edges: ordered x1, x2, weight
#Edges = (('S','A',1),('S','C',2),('C','A',4),('A','B',6),('C','D',3),('B','D',1),('B','E',2),('D','E',1))
Edges = (	('S','A',0.4),	('A','A',0.1),	('A','S',0.4),	('A','T',0.5),
			('T','A',0.6),	('T','B',0.2),	('B','T',0.5),	('B','B',0.2),
			('B','S',0.3),	('S','B',0.5),	('S','S',0.1),	('T','T',0.2))
MC = MarkovChain (Edges)
# print MC.Prob('S','A')
#print MC.GetTPM('S','A'),MC.GetTPM('S','S'),MC.GetTPM('T','B')
print MC.pathProb('S','A','A','T')
print MC.ChapmanKolmogorov('S','S',4)
print MC.StationaryDistribution()