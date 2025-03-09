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
            case "back":
                return
            case _:
                print("Invalid choice, try again")

    questions = openJson("/storage/questions.json")
    random.shuffle(questions)
    questions = questions[:15]

    saves = openJson("/storage/savedGames.json")

    while True:
        valid = True
        print("Name your save: ")
        saveName = input("> ")
        if saveName == "back":
            newGame(user)
        for entry in saves:
            if entry["user"] == user and entry["saveName"] == saveName:
                print("Already exists")
                valid = False
        if valid == True:
            break

    lastQuestion = 0
    score = 0
    createSave(saveName,user,difficulty, score, questions, lastQuestion)
    print(type(saveName))
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
    with open("/storage/savedGames.json", "r") as file:
        saves = json.load(file)

    saves.append(entry)

    with open("/storage/savedGames.json", "w") as file:
        json.dump(saves, file, indent=4)

def updateSave(name, user, difficulty, score, questions, lastQuestion):
    pass

def deleteSave(name, user):
    pass

def displaySaves(user):
    pass
def loadSave(user, saveName):
    #find the required save
    #return the save details in a list
    saves = openJson("/storage/savedGames.json")
    for entry in saves:
        if entry["user"] == user and entry["saveName"] == saveName:
            return entry