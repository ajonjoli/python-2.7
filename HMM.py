# ﻿coding=utf8
# check specially Forward and Backward algorithms
# need a better understanding of implemented algorithms
from math import fsum
import numpy as np

class HiddenMarkovModel ():
	"""docstring for HiddenMarkovModel"""
	def __init__(self, StartDistribution, TransitionDistribution, EmissionDistribution, States=None, Observations=None):
		self.StartDistribution = StartDistribution
		self.TransitionDistribution = TransitionDistribution
		self.EmissionDistribution = EmissionDistribution
		self.States = States if States else tuple(StartDistribution.keys())
		self.Observations = Observations if Observations else GetObservations()
		self.Verified = self.VerifyHMM()

	def GetObservations (self):
		Observations = set()
		for state in EmissionDistribution.values():
			Observations.update(state.keys())
		return tuple(Observations)

	def VerifyHMM (self):
		if fsum(self.StartDistribution.values()) <> 1.0:
			print 'The Start Distribution sums to',fsum(self.StartDistribution.values())
			return False
		if  len(self.States)<len(self.TransitionDistribution) or \
			len(self.States)<>len(self.TransitionDistribution):
			print 'Missing States Data'
			return False
		self.SM = [0.0]* len(self.States)	#Start Matrix
		for iNode,NodeSource in enumerate(self.States):
			if NodeSource in self.StartDistribution.keys():
				self.SM[iNode] = self.StartDistribution[NodeSource]
		self.TPM = [[0.0]* len(self.States) for s in self.States]	#Transition Probability Matrix
		for iNode,NodeSource in enumerate(self.States):
			for jNode,NodeDestiny in enumerate(self.States):
				if NodeDestiny in self.TransitionDistribution[NodeSource].keys():
					self.TPM[iNode][jNode] = self.TransitionDistribution[NodeSource][NodeDestiny]
		for row in self.TPM:
			if fsum(row)<>1:
				print row,'does not sum to 1'
				return False
		#print self.TPM
		self.EPM = [[0.0]* len(self.States) for o in self.Observations]	#Emission Probability Matrix
		for iNode,NodeDestiny in enumerate(self.Observations):
			for jNode,NodeSource in enumerate(self.States):
				if NodeDestiny in self.EmissionDistribution[NodeSource].keys():
					self.EPM[iNode][jNode] = self.EmissionDistribution[NodeSource][NodeDestiny]
		for icol in range(len(self.States)):
			if fsum([row[icol] for row in self.EPM])<>1:
				print row,'does not sum to 1'
				return False
		#print self.EPM
		return True

	def ForwardAlg (self, Sequence):
		"""
		Probability of all States after passed a sequence of observations
		ak(zk)=p(zk,x1:k)=p(xk|zk)*sum_zk-1=1^m[p(zk|zk-1)ak-1(zk-1)]
		a1(z1)=p(z1,x1)=p(x1|z1)p(z1)
		"""
		if not self.Verified:
			print 'HMM not correctly formed'
			return []
		iSeq = [self.Observations.index(obs) if obs in self.Observations else -1 for obs in Sequence]
		if -1 in iSeq:
			print iSeq.count(-1),'elements in the sequence are not observations'
			return []
		print Sequence,len(Sequence)

		ForwardMatrix = [[0.0]* len(self.States) for n in range(len(Sequence))]
		#for istate in range(len(self.States)):
		#	ForwardMatrix[0][istate] = self.EPM[istate][iSeq[0]] * self.SM[istate]
		ForwardMatrix[0] = np.array(self.EPM[iSeq[0]]) * np.array(self.SM)
		for ix in range(1,len(Sequence)):	#Dynamic Programming
			ForwardMatrix[ix] = np.dot( ForwardMatrix[ix-1], self.TPM ) * np.array(self.EPM[iSeq[ix]])

		print ForwardMatrix
		return ForwardMatrix[-1]

	def ViterbiAlg (self, Sequence):
		"""
		Given: x1:n, Compute z1:n
		z=argmax_z(p(z|x))=argmax_z(p(z,x))
		max_zn mu(zn) = max_z1:np(x1:n,z1:n)
		muk(zk)=max(p(z1:k,x1:k))=max_zk:n[p(xk|zk)p(zk|zk-1)muk-1(zk-1)]
		mu1(z1)=p(z1,x1)=p(x1|z1)p(z1)
		"""
		if not self.Verified:
			print 'HMM not correctly formed'
			return []
		iSeq = [self.Observations.index(obs) if obs in self.Observations else -1 for obs in Sequence]
		if -1 in iSeq:
			print iSeq.count(-1),'elements in the sequence are not observations'
			return []
		print Sequence,len(Sequence)

		ViterbiMatrix = [[0.0]* len(self.States) for n in range(len(Sequence))]
		ViterbiPaths = [ [ [] for s in range(len(self.States)) ] for n in range(len(Sequence)) ]
		ViterbiMatrix[0] = np.array(self.EPM[iSeq[0]]) * np.array(self.SM)
		ViterbiPaths[0] = [[state] for state in self.States]
		for ix in range(1,len(Sequence)):
			for istate in range(len(self.States)):
				temp = list( self.EPM[iSeq[ix]][istate] * np.array([row[istate] for row in self.TPM]) * ViterbiMatrix[ix-1] )
				ViterbiMatrix[ix][istate] = max(temp)
				ViterbiPaths[ix][istate] = list(ViterbiPaths[ix-1][ temp.index(max(temp)) ])
				ViterbiPaths[ix][istate].append( self.States[istate] )
			ViterbiMatrix[ix] = np.array(ViterbiMatrix[ix])

		temp = list(ViterbiMatrix[-1])
		MaxValue = max(temp)
		MaxPath = ViterbiPaths[-1][ temp.index(MaxValue) ]
		#print ViterbiPaths
		#print ViterbiMatrix
		return MaxValue,MaxPath

	def BackwardAlg (self, State, Sequence):
		"""
		Probability of a sequence of observations given certain State
		bk(zk)=p(xk+1:n|zk)=sum_zk+1=1^m[bk+1(zk+1)p(zk+1|zk)p(xk+1|zk+1)]
		bn(zn)=p(xn|zn)p(zn|zn-1)=1
		"""
		if not self.Verified:
			print 'HMM not correctly formed'
			return []
		iSeq = [self.Observations.index(obs) if obs in self.Observations else -1 for obs in Sequence]
		if -1 in iSeq:
			print iSeq.count(-1),'elements in the sequence are not observations'
			return []
		print Sequence,len(Sequence)

		BackwardMatrix = [[0.0]* len(self.States) for n in range(len(Sequence))]
		BackwardMatrix[-1] = np.array( [1.0]* len(self.States) )
		for ix in range(len(Sequence)-2,-1,-1):
			BackwardMatrix[ix] = np.dot( BackwardMatrix[ix+1] * np.array(self.EPM[iSeq[ix+1]]), self.TPM )

		print BackwardMatrix
		return BackwardMatrix[0]

StartDistribution = {'Rainy': 0.6, 'Sunny': 0.4}
TransitionDistribution = {
	'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
	'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}
EmissionDistribution = {
	'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
	'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}
States = ('Rainy', 'Sunny')
Observations = ('walk', 'shop', 'clean')

HMM1 = HiddenMarkovModel( StartDistribution, TransitionDistribution, EmissionDistribution, States, Observations )
print HMM1.States, HMM1.Observations, HMM1.Verified
Ob = Observations
#print HMM1.ForwardAlg([ Ob[1],Ob[1],Ob[2],Ob[0] ])
#print HMM1.BackwardAlg( 'Rainy', [Ob[1],Ob[1],Ob[2],Ob[0]] )
print HMM1.ViterbiAlg([ Ob[1],Ob[1],Ob[2],Ob[0] ])

"""
estructura contiene
	probabilidades estacionarias estados. Initial distribution pi
	probabilidades entre estados
	probabilidades de emisión cada estado x cada observación
	Forward Algorithm
	ak(zk)=p(zk,x1:k)=sum_zk-1=1^m[p(xk|zk)p(zk|zk-1)p(zk-1,x1:k-1)]
	a1(z1)=p(z1,x1)=p(z1)p(x1|z1)
	Backward Algorithm
	bk(zk)=p(xk+1:n|zk)=sum_zk+1=1^m[bk+1(zk+1)p(xk+1|zk+1)p(zk+1|zk)]
	bn(zn)=p(xn|zn)p(zn|zn-1)=1
	Viterbi Algorithm
	Given: x1:n, Compute z1:n
	z=argmax_z(p(z|x))=argmax_z(p(z,x))
	max_zn mu(zn) = max_z1:np(x1:n,z1:n)
	muk(zk)=max(p(z1:k,x1:k))=max[p(xk|zk)p(zk|zk-1)muk-1(zk-1)]
	mu1(z1)=p(z1,x1)=p(z1)p(x1|z1)
"""