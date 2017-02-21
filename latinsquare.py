order = int(input('Enter the order'))
number = int(input('Enter the top-left number'))

for row in range(number, order + 1):
    count = row
    for col in range(number, order+1):
        if count > order:
            print (count%order, end=' ')
        else:
            print (count, end=' ')
        count = count + 1
    print('\n')
