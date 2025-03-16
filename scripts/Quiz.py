import json
import random
import sys
import time

from SaveManagement import *
from UserManagement import *

globalHighscore = 0

questionsFile = "/Users/jeevan/Documents/Python/PythonProject/GCSE-Quiz/storage/questions.json"
def openJson(filename):
    with open(filename, "r") as file:
        return json.load(file)

def askQuestion(questions, questionNumber, difficulty):
    question = questions[questionNumber]
    choices = question["choices"]
    actualAnswer = question["answer"]
    question = question["question"]
    validAnswer = False
    print(question)
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
        elif answer == "pass" or answer == "save":
            validAnswer = True
        else:
            print("Invalid answer, try again to type pass to give up")

    if answer.lower() == actualAnswer.lower():
        if difficulty == 'easy':
            points = 2
        elif difficulty == 'medium':
            points = 3
        elif difficulty == 'hard':
            points = 5
        print(f"Correct answer! {points} awarded!")
        return points
    elif answer.lower() == "save":
        return "save"
    elif answer.lower() == "pass":
        print("Answer skipped, No points awarded.")
        return 0
    else:
        if difficulty == 'easy':
            points = 0
            print(f"Wrong! Correct answer was {actualAnswer}. No points awarded.")
        elif difficulty == 'medium':
            points = 0
            print(f"Wrong! Correct answer was {actualAnswer}. No points awarded.")
        elif difficulty == 'hard':
            points = -3
            print(f"Wrong! Correct answer was {actualAnswer}. {points} deducted.")
        return points

def game(user,save):
    questions = save["questions"]
    difficulty = save["difficulty"]
    lastQuestion = save["lastQuestion"]
    savedScore = save["score"]
    saveName = save["saveName"]
    i=lastQuestion
    score = savedScore
    while True:
        if i>5:
            print(f"End of quiz, final score = {score}")
            updateSave(saveName, user, score, i)
            return True
        output = askQuestion(questions, i, difficulty)
        if output == "save" or output == "back":
            updateSave(saveName,user,score,i)
            print("Saving game")
            return False
        else:
            score += output
        print(i)
        i+=1




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
                if saveName == False:
                    continue
                save = loadSave(user,saveName)
                game(user,save)

            case "3":
                if loginStatus == "Login":
                    print("You are not logged in, returning to menu...")
                    time.sleep(0.75)
                    menuLoop()
                saveName = displaySaves(user)
                if saveName == None:
                    continue
                else:
                    save = loadSave(user,saveName)
                    game(user,save)
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
                deleteSave("test", "tecknet")
                pass
            case "debug3":
                displaySaves("tecknet")
            case _:
                print("Invalid choice, returning to menu")

menuLoop()

