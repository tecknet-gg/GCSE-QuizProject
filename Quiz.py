import json
import random
import sys

from UserManagement import *

def openJson(filename):
    with open(filename, "r") as file:
        return json.load(file)

def askQuestion(questions, questionNumber, difficulty):
    question = questions[questionNumber]
    validAnswer = False
    print()
    print(question["question"])
    choices = question["choices"]
    random.shuffle(choices)

    for i in range(len(choices)):
        print(f"{chr(i+65)}. {choices[i]}")

    while validAnswer == False:
        answer = input("Answer: ").lower()
        if answer == 'a' or answer == 'b' or answer == 'c' or answer == 'd':
            answer = choices[ord(answer)-97]
            validAnswer = True
        elif answer == choices[0].lower() or answer == choices[1].lower() or answer == choices[2].lower() or answer == choices[3].lower():
            validAnswer = True
        elif answer == 'pass':
            validAnswer = True
        else:
            print("Invalid answer, try again to type pass to give up")

    if answer.lower() == question["answer"].lower():
        if difficulty == 'easy':
            points = 2
        elif difficulty == 'medium':
            points = 3
        elif difficulty == 'hard':
            points = 5
        print(f"Correct answer! {points} awarded!")
        return points
    else:
        if difficulty == 'easy':
            points = 0
            print(f"Wrong! Correct answer was {question['answer']}. No points awarded.")
        elif difficulty == 'medium':
            points = 0
            print(f"Wrong! Correct answer was {question['answer']}. No points awarded.")
        elif difficulty == 'hard':
            points = -3
            print(f"Wrong! Correct answer was {question['answer']}. {points} deducted.")
        return points


def menuLoop():
    loginStatus = "Login"
    user = None
    while True:
        print()
        print("Menu:")
        if loginStatus == "Logout":
            print(f"User: {user} ")
        else:
            print("User - Not logged in")
        print(f"1 - {loginStatus}")
        print("2 - New Game")
        print("3 - Load Game")
        print("4 - Leaderboard")
        print("5 - Register new user")
        print("6 - Quit")
        choice = input("Choice: ")
        match choice:
            case "1":
                if loginStatus == "Login":
                    user = login()
                    loginStatus = f"Logout"
                else:
                    print("Logging out...")
                    loginStatus = "Login"
                    user = None
            case "2":
                questions = openJson("questions.json")
                random.shuffle(questions)
                print(type(questions))
                askQuestion(questions, 1, "hard")
            case "3":
                print("Loading Game...")
            case "4":
                print("Leaderboard")
            case "5":
                print("Registering...")
                registerUser()
            case "6":
                print("Exiting")
                sys.exit(0)
            case _:
                print("Invalid choice, returning to menu")
                menuLoop()

menuLoop()

