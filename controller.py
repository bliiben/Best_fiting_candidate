from Dimension import Dimension
from Population import Population
from Candidat import Candidat
import pickle
import sys
dimensions = []
populations = []
candidats = []

def menu():
	# Display current setup
	if(len(dimensions)):
		print ("\nSubjetcs  :")
		for d in dimensions:
			print "\t- "+d.name
	if(len(populations)):
		print ("\nPopulations")
		for p in populations:
			print "\t- "+p.name+" ("+str(p.size)+")"
	if(len(candidats)):
		print ("\nCandidats")
		for c in candidats:
			print "\t- "+c.name

	# Save to a temporary file
	file = open("lastSave.j","wb")
	pickle.dump({"dimensions" : dimensions, "populations" : populations, "candidats" : candidats }, file)
	file.close()

	# Choose a menu
	inp = None
	while ( inp not in map(str,range(5))):
		print("\n\n[0] Subjects")
		print("[1] Population")
		print("[2] Candidat")
		print("[3] Setup")
		print("[4] Go")
		inp = raw_input("")
	return int(inp)

def setDimensions():
	print("Setting Subjects...\n")
	dimensions.append(Dimension(raw_input("Subject name : ")))

def setPopulation():
	print("Setting Population...\n")
	populations.append(Population(raw_input("Population name : "),float(raw_input("Population number : "))))

def setCandidats():
	print("Setting Candidats...\n")
	candidats.append(Candidat(raw_input("Candidat name : ")))

# Run the setup and inserts values into the variables
def setup():
	print("Setup...\n")
	for dimension in dimensions:
		for population in populations:
			inp=""
			while(inp.lower() not in ["y","n"]):
				inp = raw_input("Population "+population.name+" in dimension" + dimension.name + " ? Y/N")

			if(inp.lower() == "y"):
				importance = float(raw_input("Importance [0-100] : "))
				position = int(raw_input("Position [0-100] : "))
				clout = int(raw_input("Clout [0-100+ : "))
				dimension.addPopulation( population, importance=importance, position = position, clout=clout)

	for dimension in dimensions:
		for candidat in candidats:
			inp=""
			while(inp.lower() not in ["y","n"]):
				inp = raw_input("Candidat "+candidat.name+" in dimension" + dimension.name + " ? Y/N")

			if(inp.lower() == "y"):
				dimension.addCandidate( candidat , int(raw_input("Position [0-100]")))


# Calculate the result
def go():
	print("Go...\n")
	for dimension in dimensions:
		dimension.calculatePoints()

	for candidat in candidats :
		votes = 0.0
		for population in populations:
			popVote = population.getPopulationVote()
			if( candidat in popVote ):
				votes += popVote[candidat]


		print candidat.name + " has " + str(votes) + " votes"

def switcher( inp ):
	funcs = [setDimensions, setPopulation, setCandidats, setup, go]
	funcs[inp]()

if __name__ == '__main__':
	# Load save file if passed
	if( len(sys.argv) >= 2 ):
		file = open(sys.argv[1],"rb")
		data = pickle.load( file )
		file.close()
		dimensions = data["dimensions"]
		populations = data["populations"]
		candidats = data["candidats"]
	# Run menu and await for another function
	while(True):
		switcher ( menu() )