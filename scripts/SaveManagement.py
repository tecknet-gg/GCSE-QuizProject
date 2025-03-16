import random
import json


savesFile = "/Users/jeevan/Documents/Python/PythonProject/GCSE-Quiz/storage/savedGames.json"
questionsFile = "/Users/jeevan/Documents/Python/PythonProject/GCSE-Quiz/storage/questions.json"

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
                return False
            case _:
                print("Invalid choice, try again")

    questions = openJson(questionsFile)
    random.shuffle(questions)
    questions = questions[:15]

    saves = openJson(savesFile)

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
    with open(savesFile, "r") as file:
        saves = json.load(file)

    saves.append(entry)

    with open(savesFile, "w") as file:
        json.dump(saves, file, indent=4)

def updateSave(name, user, score, lastQuestion):
    saves = openJson(savesFile)
    for entry in saves:
        if entry["user"] == user and entry["saveName"] == name:
            entry["score"] = score
            entry["lastQuestion"] = lastQuestion
            break
    file = openJson(savesFile)
    with open(savesFile, "w") as file:
        json.dump(saves, file, indent=4)

    pass

def deleteSave(name, user):
    saves = openJson(savesFile)
    for entry in saves:
        if entry["user"] == user and entry["saveName"] == name:
            del saves[saves.index(entry)]
    file = openJson(savesFile)
    with open(savesFile, "w") as file:
        json.dump(saves, file, indent=4)


def displaySaves(user):
    saves = openJson(savesFile)
    userSaves = []
    for entry in saves:
        if entry["user"] == user:
            print(f"{saves.index(entry)+1}. Save: {entry["saveName"]}   Questions completed: {entry["lastQuestion"]+1}   Score: {entry["score"]}")
            userSaves.append(entry["saveName"])
    if len(userSaves) == 0:
        print("No saves found")
        return None
    while True:
        saveChoice = input("> ")
        if saveChoice == "back":
            return None
        elif saveChoice in userSaves:
            return saveChoice
        elif saveChoice.isdigit() and 1 <= (int(saveChoice)-1) <= len(userSaves):
            return userSaves[int(saveChoice)-1]
        else:
            print("Invalid choice, try again")

def loadSave(user, saveName):
    saves = openJson(savesFile)
    for entry in saves:
        if entry["user"] == user and entry["saveName"] == saveName:
            return entry
    return None