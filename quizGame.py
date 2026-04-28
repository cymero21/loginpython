questions = [ "what is 2+2?", "your last name?", "favorite food?" ]
answers = ["4", "ayobami", "beans"]

score = 0

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")

    if user_answer.lower() == answers[i]:
        print("correct")
        score += 1
    else:
        print("wrong")

print( "final sccore:", score, "/", len(questions))