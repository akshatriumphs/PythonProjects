print('This is a puzzle favored by Einstein. You will be asked to enter a three digit number, where the hundreds digit differs from the ones digit by at least two. The procedure will always yield 1089')
number = int(input('Give me a number: '))
k = number
reverse = 0
while number != 0:
    remainder = number%10
    reverse = (reverse*10) + remainder
    number = int(number/10)

print ('For the number: ', k, 'the reverse number is:', reverse)
if k >= reverse:
    print('The difference between ',k,' and ',reverse,' is ', k - reverse)
    l = k - reverse
else:
    print('The difference between ',reverse,' and ',k,' is ', reverse - k)
    l = reverse - k
j = l
reverse_difference = 0
while l != 0:
    r = l%10
    reverse_difference = (reverse_difference*10) + r
    l = int(l/10)

print ('The reverse difference is: ', reverse_difference)
print ('The sum of: ', j,' and revDiff is: ', j+reverse_difference)


    
    
