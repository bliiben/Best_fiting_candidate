This code is there to find how many votes each condidate will receive, by analysing the electorate on subject that are discussed during the election campain. Considering the importance of each question for the electorate and their willingness to compromise on the subject.

Run controller.py

Example : 

Set a few Subject
> 0
> Work

> 0
> Ecology

Set a few population
> 1
> Young
> 20

> 1
> Old
> 30

Set some candidate
> 2
> Joseph

> 2
> Andree

That is the current setup : 

Subjetcs  :
	- Work
	- Ecology

Populations
	- Young (20.0)
	- Old (30.0)

Candidats
	- Joseph
	- Andree

Run 3 - Setup.
On each subject we setup for each population, we setup the importance of a question. 0 not important, 100 very important. We setup their position on the spectre. 0 one side of the specter, 100 the other side of the spectre. We setup the clout, wich is how much they are willing to compromise. 50 correspond to a willingness to compromise to a position 50+ and 50- from their current position.
After we setup the position of each candidate.

> Population Young in dimensionWork ? Y/NY
> Importance [0-100] : 80
> Position [0-100] : 95
> Clout [0-100+ : 60
> 
> Population Old in dimensionWork ? Y/NY
> Importance [0-100] : 20
> Position [0-100] : 30
> Clout [0-100+ : 80
> 
> Population Young in dimensionEcology ? Y/NY
> Importance [0-100] : 50
> Position [0-100] : 75
> Clout [0-100+ : 35
> 
> Population Old in dimensionEcology ? Y/NY
> Importance [0-100] : 75
> Position [0-100] : 55
> Clout [0-100+ : 35
> 
> Candidat Joseph in dimensionWork ? Y/NY
> Position [0-100]35
> Candidat Andree in dimensionWork ? Y/NY 
> Position [0-100]95
> Candidat Joseph in dimensionEcology ? Y/NY
> Position [0-100]80 
> Candidat Andree in dimensionEcology ? Y/NY
> Position [0-100]60

This calculate the number of votes for each candidate.
4 - Go

> Joseph has 13.4663326177 votes
> Andree has 36.5336673823 votes
