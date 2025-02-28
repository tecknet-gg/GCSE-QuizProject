import json
import random
import sys

from UserManagement import *

def openJson(filename):
    with open(filename, "r") as file:
        return json.load(file)

def askQuestion(number, difficulty):

    questions = openJson("questions.json")
    random.shuffle(questions)
    question = questions[0]
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
        print(f"Correct! +1 points.")
        return True
    else:
        print(f"Wrong! Correct answer was {question['answer']}")
        return False


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
        print("2 - Register")
        print("3 - Load Game")
        print("4 - New Game")
        print("5 - Leaderboard")
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
                print("Registering...")
                registerUser()
            case "3":
                askQuestion(1,"hard")
            case "4":
                print("Load Game")
            case "5":
                print("Leaderboard")
            case "6":
                print("Exiting")
                sys.exit(0)
            case _:
                print("Invalid choice, returning to menu")
                menuLoop()

menuLoop()

