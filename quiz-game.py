import random

questions = {
    "What is the capital of India?": "Delhi",
    "What is 5 + 5?": "10",
    "Which language is used for web development?": "HTML"
}

score = 0

print("===== QUIZ GAME =====")

for question, answer in questions.items():
    print("\n" + question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", answer)

print("\nYour Score:", score, "/", len(questions))