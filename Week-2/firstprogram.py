import math
import random as r

print('Guess a number between 1 and 5')
user_guess = input()
user_guess = int(user_guess)

if user_guess == r.randint(1,5):
    print('i got it right!')
else:
    print('i got it wrong...')
    