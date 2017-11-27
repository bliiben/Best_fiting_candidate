class Population():
	def __init__(self, name, size):
		self.name = name
		self.size = float(size)
		self.candidatesPoints = []
	
	def candidateAdd( self, candidate, points ):

		for c in self.candidatesPoints:
			if( c["candidate"] == candidate):
				c["points"] = c["points"] + points
				
				return
		self.candidatesPoints.append( {"candidate" : candidate , "points" : points } )

	def __str__( self ):
		total = 0.0
		for c in self.candidatesPoints:
			total = total + c["points"]

		sCan = ""
		for c in self.candidatesPoints:
			sCan = sCan + "\n" + str(c["candidate"]) + " " + str((float(c["points"])/total)*self.size) + " votes"

		return "\n-" +self.name + "-\n" + sCan

	def getPopulationVote( self ):
		total = 0.0
		for c in self.candidatesPoints:
			total = total + c["points"]

		sCan = {}
		for c in self.candidatesPoints:
			sCan[c["candidate"]] = (float(c["points"])/total)*self.size
		return sCan