import math
T = float(input('Please enter the temperature(degrees F): '))
W = float(input('Please enter the wind speed(MPH): '))
WCT = 35.74 + 0.6215*T - 35.75*W**0.16 + 0.4275*T*W**0.16
print ('Wind Chill Temperature Index: ', WCT)
