guess = 0
tries = 0

while guess != 7 and tries < 5:
    guess = int(input('Guess the number: '))
    tries = tries + 1

if guess != 7:
    print('You rant out of tries')

else:
    print('You guessed the number')
    