char = input('Customers code')
begin_reading = float(input('Enter beginning meter reading: '))
end_reading = float(input('Enter ending meter reading: '))
if end_reading > begin_reading:
    if char == 'r':
        cost = 5 + float(0.0005 * (end_reading-begin_reading))
    elif char == 'c':
        cost = 1000 + float(0.00025 * (end_reading-begin_reading-4))
    elif char == 'i':
        if end_reading - begin_reading < 4:
            cost = 1000
        elif end_reading - begin_reading > 4 and end_reading - begin_reading < 10:
            cost = 2000
        elif end_reading - begin_reading > 10:
            cost = 2000 + float(0.00025 * (end_reading - begin_reading - 10))
print (cost)
