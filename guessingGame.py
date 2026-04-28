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

questions = ["2 + 2?", "Capital of France?", "5 * 3?"]
answers = ["4", "paris", "15"]

score = 0

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")

    if user_answer.lower() == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Final score:", score, "/", len(questions))