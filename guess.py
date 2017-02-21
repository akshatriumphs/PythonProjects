print ('We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!')
player1 = int(input('This will be the answer. Select a number 10-49: '))
player2 = int(input('Pick any number 50-99: '))
factor = 99 - player1
factor1 = factor + player2
j = int(factor1/100)
k = factor1%100
factor2 = k + j
answer = player2 - factor2
print ('I said the answer was ',answer,' and the calculation result is ',answer)
