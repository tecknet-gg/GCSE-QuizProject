import time
import json
import datetime

userFile = "/Users/jeevan/Documents/Python/PythonProject/GCSE-Quiz/storage/users.json"
leaderboardFile = "/Users/jeevan/Documents/Python/PythonProject/GCSE-Quiz/storage/leaderboard.json"

def openJson(filename):
    with open(filename, "r") as file:
        return json.load(file)

def addScore(user,score,difficulty):
    entry = {
        "user": user,
        "score": score,
        "difficulty": difficulty,
        "time": round(time.time())
    }
    scores = openJson(leaderboardFile)
    scores.append(entry)
    with open(leaderboardFile, "w") as file:
        json.dump(scores, file, indent=4)


def displayGlobalTable():
    scores = openJson(leaderboardFile)
    scores = sorted(scores, key=lambda entry: (-entry["score"], entry["time"]))

    users = []
    for entry in scores:
        users.append(len(entry["user"]))
    userWidth = round(max(users)*1.5)

    headers = ["User", "Score", "Difficulty", "Time"]
    columnWidths= [userWidth,8,14,12]

    print(f"{headers[0].ljust(columnWidths[0])}{headers[1].ljust(columnWidths[1])}{headers[2].ljust(columnWidths[2])}{headers[3].ljust(columnWidths[3])}")
    print("_" * sum(columnWidths))
    for entry in scores:
        print(f"{entry["user"].ljust(columnWidths[0])}{str(entry["score"]).ljust(columnWidths[1])}{entry["difficulty"].ljust(columnWidths[2])}{str((datetime.datetime.fromtimestamp(entry["time"])).strftime("%d-%m-%Y")).ljust(columnWidths[3])}")

def displayPersonalTable(user):
    scores = openJson(leaderboardFile)
    userScores = []
    for entry in scores:
        if entry["user"] == user:
            userScores.append(entry)

    users = []
    for entry in userScores:
        users.append(len(entry["user"]))
    userWidth = round(max(users) * 1.5)

    headers = ["User", "Score", "Difficulty", "Time"]
    columnWidths = [userWidth, 8, 14, 12]

    print(
        f"{headers[0].ljust(columnWidths[0])}{headers[1].ljust(columnWidths[1])}{headers[2].ljust(columnWidths[2])}{headers[3].ljust(columnWidths[3])}")
    print("_" * sum(columnWidths))
    for entry in userScores:
        print(
            f"{entry["user"].ljust(columnWidths[0])}{str(entry["score"]).ljust(columnWidths[1])}{entry["difficulty"].ljust(columnWidths[2])}{str((datetime.datetime.fromtimestamp(entry["time"])).strftime("%d-%m-%Y")).ljust(columnWidths[3])}")

def findGlobalHighscore():
    scores = []
    data = openJson(leaderboardFile)
    for entry in data:
        scores.append(entry["score"])
    return scores[scores.index(max(scores))]


