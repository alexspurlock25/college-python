# Alexander Spurlock

import random

compNum = random.randint(1, 51)
print('(DEBUGGING) Random Number: % s' % compNum)

# loop while the user is not correct
correct = False
while correct is False:
    guess = int(input('Please guess a number between 1 and 50: '))

    if guess > compNum:
         print('Too high. Try again.')

    if guess < compNum:
        print('Too low. Try again.')

    if guess == compNum:
        print('Correct.')
        # flip the boolean to exit the loop when the user is correct
        correct = True
