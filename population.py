year = int(input('How many years '))
totalSec = 31536000
birth = int((31536000*year)/7)
death = int((31536000*year)/13)
immigrant = int((31536000*year)/35)
population = 307357870
newPopulation = population + birth + immigrant - death
print (newPopulation)
