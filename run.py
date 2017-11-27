from Dimension import Dimension
from Population import Population
from Candidat import Candidat

jeanLuc = Candidat("Jean-luc")
marieRenee = Candidat("Marie-Renee")

ecology = Dimension("Ecology")
jobs = Dimension("Jobs")
infrastructure = Dimension("Infrastructure")

catholics = Population("Catholics", 30)
youngEducated = Population("Young educated", 20)

ecology.addPopulation( catholics, importance=15, position = 75, clout=35)
ecology.addPopulation( youngEducated, importance=50, position = 99, clout=15)

jobs.addPopulation( catholics, importance=12, position = 99, clout=25)
jobs.addPopulation( youngEducated, importance=20, position = 99, clout=70)

infrastructure.addPopulation( catholics, importance=70, position = 99, clout=30)
infrastructure.addPopulation( youngEducated, importance=70, position = 5, clout=50)

ecology.addCandidate(marieRenee,85)
jobs.addCandidate(marieRenee,99)
infrastructure.addCandidate(marieRenee,99)

ecology.addCandidate(jeanLuc,97)
jobs.addCandidate(jeanLuc,99)
infrastructure.addCandidate(jeanLuc,0)

ecology.calculatePoints()
jobs.calculatePoints()
infrastructure.calculatePoints()

print catholics, youngEducated