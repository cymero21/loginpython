import random

secret = random.randint(1, 30)
attempts = 5

while attempts > 0:
    guess = int(input(" guess a number between 1 and 30:"))

    if guess == secret:
        print("you win")
        break
    elif guess > secret:
        print("too high")
    else:
        print("too low")

    attempts -= 1
    print( attempts, " attempts remaining")

if attempts == 0:
    print (" you lost, answer is", secret)

# This code is a simple guessing game where the user has to ]
# guess a random number between 1 and 30.
# The user has five attempts to guess the correct number. 
# After each guess, the program provides