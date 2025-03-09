import json
import random
import sys
import time

from SaveManagement import *
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
        choice = input("> ")
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
                if loginStatus == "Login":
                    print("You are not logged in, returning to menu...")
                    time.sleep(0.75)
                    menuLoop()
                saveName = newGame(user)
                save = loadSave(user,saveName)
                questions = [(i["question"], i["choices"], i["answer"]) for i in loadSave(user, saveName)["questions"]]

            case "3":
                questions = openJson("/storage/questions.json")
                random.shuffle(questions)
                questions = questions[:15]
                askQuestion(questions,1,"easy")
            case "4":
                print("Leaderboard")
            case "5":
                print("Registering...")
                registerUser()
            case "6":
                print("Exiting")
                sys.exit(0)
            case "debug1":
                user = "bob"
                saveName = newGame(user)
                print(loadSave(user,saveName))
            case "debug2":
                pass
            case _:
                print("Invalid choice, returning to menu")

menuLoop()

