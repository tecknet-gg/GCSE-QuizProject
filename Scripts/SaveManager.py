import random
import json

def openJson(filename):
    with open(filename, "r") as file:
        return json.load(file)

def newGame(user):
    while True:
        print("Select difficulty: ")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Back")
        choice = input("> ")
        match choice:
            case "1":
                difficulty = "easy"
                break
            case "2":
                difficulty = "medium"
                break
            case "3":
                difficulty = "hard"
                break
            case "4":
                return
            case _:
                print("Invalid choice, try again")

    questions = openJson("questions.json")
    random.shuffle(questions)
    questions = questions[:15]

    print("Create name for save state :")
    saveName = input("> ")
    lastQuestion = 0
    score = 0
    createSave(saveName,user,difficulty,score,questions, lastQuestion)
    return saveName

def createSave(name, user, difficulty, score, questions, lastQuestion):
    entry = {
        "user": user,
        "saveName": name,
        "difficulty": difficulty,
        "score": score,
        "questions": questions,
        "lastQuestion": lastQuestion
    }
    with open("savedGames.json", "r") as file:
        saves = json.load(file)

    saves.append(entry)

    with open("savedGames.json", "w") as file:
        json.dump(saves, file, indent=4)

def updateSave(name, user, difficulty, score, questions, lastQuestion):
    pass

def deleteSave(name, user):
    pass

def displaySaves(user):
    pass