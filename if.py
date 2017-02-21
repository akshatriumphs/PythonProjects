import math
richter = float(input('Enter the richter scale: '))
y = float(1.5 * richter) + 4.8
Joules = math.pow(10.0, y)
print ('Energy in Joules: ', Joules)
TNT = Joules/4184000000
print ('TNT: ', TNT)


