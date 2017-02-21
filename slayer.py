print('Guess a six-digit number SLAYER so that following equation is true,where each letter stands for the digit in the position shown:SLAYER + SLAYER + SLAYER = LAYERS ')
number = int(input('Enter your guess for SLAYER: '))
if number//100000 == 0:
    print('Your guess is incorrect: SLAYER must be a 6-digit number.')
else:    
    sum = number/100000
    remainder = int(((number%100000)*10)+sum)
    new_number = 3 * number
    print(remainder)
    if new_number == remainder:
        print('Your guess is correct')

print ('Thanks for playing')
    
