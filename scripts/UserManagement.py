import json

def openJson(filename):
    with open(filename, "r") as file:
        return json.load(file)

def addUser(details, filename):
    with open(filename,"w") as file:
        json.dump(details, file, indent=4)

def login():
    attempts = 100
    details = {user["username"]: user["password"] for user in openJson("/storage/users.json")}
    loggedIn = False
    for _ in range(attempts):
        if loggedIn:
            break
        username = input("Username: ")
        if username == "back":
            break
        if username in details:
            for _ in range(attempts):
                password = input("Password: ")
                if password == "back":
                    break
                if password == details[username]:
                    print("Logged in as " + username)
                    return (username)
                else:
                    print("Wrong password")
        else:
            print("Username not found")

def registerUser():
    attempts = 3
    details = openJson("/storage/users.json")
    while True:
        username = input("Username: ")
        if username == "back":
            break
        if validateUser(username) == 1:
            print("Username taken")
            continue
        elif validateUser(username) == 2:
            print("Username can only contain alphanumeric characters and '@' or '_' and must be 6 characters or longer")
            continue
        elif validateUser(username) == 3:
            print("Valid username")
            while True:
                password = input("Password: ")
                if password == "back":
                    break
                if validatePassword(password):
                    print("Valid password, saving details and returning to menu")
                    newEntry = {"username": username,
                                "password": password,
                                "highscore": "0"}
                    details.append(newEntry)
                    addUser(details, "/storage/users.json")
                    return True

        else:
            return False

def validateUser(username):
    details = {user["username"] for user in openJson("/storage/users.json")}
    if username.lower() in details:
        return 1
    elif (username.isalnum() or "@" in username or "_" in username) and len(username) > 4:
        if len(username) < 4:
            print("Username is too short")
        return 3
    else:
        return 2

def validatePassword(password):
    if (password.isalnum() or "@" in password or "_" in password) and len(password) > 6:
        return True
    elif len(password)<6:
        print("Password too short")
        return False
    else:
        print("Password can only contain alphanumeric characters and '@' or '_'")
        return False