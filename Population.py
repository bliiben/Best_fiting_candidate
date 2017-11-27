class Population():
	def __init__(self, name, size):
		self.name = name
		self.size = float(size)
		self.candidatesPoints = []
	
	# Add the points for each candidate depensing of the population
	def candidateAdd( self, candidate, points ):
		for c in self.candidatesPoints:
			if( c["candidate"] == candidate):
				c["points"] = c["points"] + points
				return

		self.candidatesPoints.append( {"candidate" : candidate , "points" : points } )

	# Display how much a population vote for each candidate
	def __str__( self ):
		total = 0.0
		for c in self.candidatesPoints:
			total = total + c["points"]

		sCan = ""
		for c in self.candidatesPoints:
			sCan = sCan + "\n" + str(c["candidate"]) + " " + str((float(c["points"])/total)*self.size) + " votes"

		return "\n-" +self.name + "-\n" + sCan

	# Return total vote for a candidate
	def getPopulationVote( self ):
		total = 0.0
		for c in self.candidatesPoints:
			total = total + c["points"]

		sCan = {}
		for c in self.candidatesPoints:
			sCan[c["candidate"]] = (float(c["points"])/total)*self.size
		return sCan