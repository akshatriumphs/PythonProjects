n= int(input('Please give me an integer'))
r = 0
while n!= 0:
    r = r + n%10
    n = int(n/10)
    if r/10 == 0:
        break
    else:
        n = r
        continue

print (r)
        
