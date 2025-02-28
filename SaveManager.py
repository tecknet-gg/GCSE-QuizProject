from UserManagement import *
import random

def newGame(user):
    while True:
        print("Select difficulty: ")
        print("1. Easy")
        print("2. Normal")
        print("3. Hard")
        print("4. Back")
        choice = input("> ")
        match choice:
            case "1":
                difficulty = easy
                break
            case "2":
                difficulty = normal
                break
            case "3":
                difficulty = medium
                break
            case "4":
                return
            case _:
                print("Invalid choice, try again")

    questions = openJson("questions.json")
    print("Create name for save state :")
    name = input("> ")
    lastQuestion = 0
    score = 0
    return (createSave(name,user,difficulty,score,questions, lastQuestion))

def createSave(name, user, difficulty, score, questions, lastQuestion):
    entry = {
        "user": user,
        "saveName": name,
        "difficulty": difficulty,
        "score": score,
        "questions": questions,
        "lastQuestion": lastQuestion
    }
    with open("saved_games.json", "r") as file:
        saves = json.load(file)
    saves.append(entry)
    with open("saved_games.json", "w") as file:
        json.dump(saves, file, indent=4)

def updateSave(name, user, difficulty, score, questions, lastQuestion):
    pass

def deleteSave(name, user):
    pass

def displaySaves(user):
    pass
newGame("test")