print('This is a puzzle favored by Gen. MacArthur. You will be asked to secretly type in your birth month (as an integer) and your age. The computer will make a special calculation, yielding a new integer and calculate your birth month and age')
month = int(input('Give me your birth month: '))
age = int(input('Give me your age: '))
new_age1 = 2*month
new_age2 = new_age1 + 5
new_age3 = new_age2 * 50
new_age4 = new_age3 + age
new_age5 = new_age4 - 365
print ('The special number is: ', new_age5)
new_age6 = new_age5 + 115
month_new = int(new_age6/100)
age_new = int(new_age6%100)
print ('The computer calculates that you were born in the ',month_new,' and are ',age_new,' years old')
