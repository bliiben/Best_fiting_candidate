from math import pi, sin
class Dimension():

	def __init__(self, name):
		self.name = name
		self.populations = []
		self.candidates = []
		self.PRECISION = 100
	def addPopulation( self, population, importance, position, clout ):
		self.populations.append( { "population" : population, "graph" : self.powerFunction( position, importance, clout ) } )
	def addCandidate( self, candidate, position ):
		self.candidates.append( {"candidate" : candidate, "position": position})

	def calculatePoints( self ):
		for population in self.populations:
			for candidate in self.candidates:
				population["population"].candidateAdd( candidate["candidate"] ,population["graph"][ candidate["position"] ] )
				#print( population["population"].name, candidate["candidate"].name, population["graph"][ candidate["position"] ], self.name)


	def powerFunction( self, position, importance, clout ):		
		graph = [0] * self.PRECISION
		
		start = position - ( clout / 2)
		end = position + ( clout / 2)

		if( position >= end or position <= start):
			return graph
		for x in range( 0,self.PRECISION):
			graph[x] = min(sin( ( min( position , max( start , x) ) - ( start ) )*pi / ( position-start ) / 2 ) * (importance) , sin( ( min( position + (end-position), max( position , x) )-( position - (end-position)) )* pi / (end-position) /2) *(importance) )
		return graph