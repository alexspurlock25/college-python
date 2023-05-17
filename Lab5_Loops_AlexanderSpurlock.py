import random

max_guess = 3
num_guess = 0
random_num = random.randint(1, 50)

print('(FOE TESTING) Random number: % s' % random_num)

while num_guess < max_guess:
    user_guess = int(input('Guess a number between 1 and 100: '))
    num_guess += 1

    if user_guess > random_num:
        user_guess = int(input('Too High. Try again: '))
        num_guess += 1

    if user_guess < random_num:
        user_guess = int(input('Too Low. Try again: '))
        num_guess += 1
        
    if user_guess == random_num:
        print('You win!')
        break

  
else:
    print('Game Over.')
        

