import os


usernames = []  # List of all usernames
passwords = []  # List of all passwords
attempts = 3  # Number of attempts to input valid credentials

filePath = "//Programs/Password/credentials.txt"


def readDetails():  # Reads the details from credentials.txt and appends it to the usernames and passwords lists
    usernames.clear()
    passwords.clear()
    with open(filePath, 'r') as file:  # Reads credentials written to credentials.txt
        for line in file:
            username, password = line.strip().split(',')
            usernames.append(username)
            passwords.append(password)


def deleteLine(line):
    line -= 1
    with open(filePath, 'r') as file:
        lines = file.readlines()
    if 0 <= line < len(lines):
        del lines[line]
    else:
        print("Invalid line number")
        return
    with open(filePath, 'w') as file:
        file.writelines(lines)


def getSmaller(input):  # Turns all the uppercase characters in a string to lowercase
    charList = list(input)
    length = len(charList)
    for i in range(length):
        if ord(charList[i]) >= 65 and ord(charList[i]) <= 90:
            charList[i] = chr(ord(charList[i]) + 32)
        else:
            continue
    output = ''.join(charList)
    return output


def writeDetails(userName, password):  # Writes validated credentials to credentials.txt
    with open(filePath, 'a') as file:
        file.write(f"{userName},{password}\n")


def checkCharacters(input):  # Checks to see if input is utilizing invalid characters
    for i in input:
        if not (i.isalnum() or i in ['_', '@']):
            return False
    return True


def registerUsername():  # Provides an interface for the user to input a valid username
    readDetails()
    username = input("Username: ")
    if not checkCharacters(username):
        print("Username cannot contain special characters")
        return False
    for i in usernames:
        if getSmaller(i) == getSmaller(username):
            print("Username taken")
            return False
    return username


def registerPassword():  # Provides an interface for the user to input a valid password
    readDetails()
    password = input("Password: ")
    if not checkCharacters(password):
        print("Password cannot contain special characters")
        return False
    if len(password) < 6:
        print("Password must be at least 6 characters")
        return False
    else:
        return password


def registerDetails():  # Registers new login details
    readDetails()
    for i in range(1000000):
        if i%3 == 0 and i>0:
            choice = input("Return to main menu? y/n: ")
            if choice == 'y':
                return False
        readDetails()
        username = registerUsername()
        if username != False:
            break
    for i in range(100000):
        if i%3 == 0 and i>0:
            choice = input("Return to main menu? y/n: ")
            if choice == 'y':
                return False
        password = registerPassword()
        if password != False:
            break
    if (password != False and username != False):
        writeDetails(username, password)
        print("Details successfully saved")
        return True


def findIndex(username):  # Finds the corresponding password for a username
    for i in range(len(usernames)):
        if username == usernames[i]:
            return i
    return False


def login():  # Provides a way for users to log in by entering a valid username and password
    readDetails()
    # Username validation: Allow 3 attempts
    for i in range(attempts):
        username = input("Enter username: ")
        i = findIndex(username)
        if username_index is not False:
            # Password validation: Allow 3 attempts
            for j in range(attempts):
                password = input("Enter password: ")
                if passwords[j] == password:
                    print("Login successful!")
                    return True
                else:
                    print(f"Invalid password. Attempts remaining: {attempts - password_attempts - 1}")
            print("Too many incorrect password attempts. Returning to main menu.")
            return False
        else:
            print(f"Invalid username. Attempts remaining: {attempts - username_attempts - 1}")

    print("Too many incorrect username attempts. Returning to main menu.")
    return False


print()
print("Welcome to AQA User Registration")
print()


def mainMenu():  # Main menu loop
    while True:
        readDetails()
        print("##################################################################")
        print("Please enter a menu choice:")
        print("1. Login with existing username and password")
        print("2. Register new username and password")
        print("3. Exit the program")
        print("##################################################################")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        match option:
            case 1:  # Login
                if login():
                    print("Welcome back!")
                else:
                    print("Returning to main menu.")
            case 2:  # Register details
                if not registerDetails():
                    print("Out of attempts. Returning to main menu.")
                else:
                    print("Registration successful!")
            case 3:  # Exit program
                print("Exiting program. Goodbye!")
                exit()
            case _:  # Handles incorrect choices
                print("Invalid input. Please choose a valid option.")

mainMenu()