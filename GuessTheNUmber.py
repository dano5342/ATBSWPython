#This is a guess the number game.
import random

print('Hello, what is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20.') 
secret = random.randint(1, 20)

#Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    if guessesTaken > 1:
        print('Nope! Try again!')
    else:
        print('take a guess.')
    guess = int(input())
            
    if guess < secret:
        print('Your guess is too low.')
    elif guess > secret:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess.

if guess == secret:
    print('Good Job ' + name +  '. You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secret))
    
