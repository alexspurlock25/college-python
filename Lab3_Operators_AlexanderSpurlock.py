result = 0

userName = input('What is your name? ')

try:
    userNum = int(input('Hello, ' + userName + '. Enter a number: '))
    result = (((userNum + 3) * 2 - 4) // 2) - userNum
    print('Result: % s' % (result))
except:
    print("You're only allowed to enter numbers... Try again.")
