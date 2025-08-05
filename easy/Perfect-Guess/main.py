from random import randint

# variables 

randomNum = 0
guess = 10 


# this function prints the welcome message, rules and instruction.
def instructions():
    print("""
---------- WELCOME TO PERFECT GUESS GAME -----------
INSTRUCTIONS: 
    1. you have to guess a number between 1 to 100.
    2. you have 10 chances to guess it.
    3. hint will also be provided to guess the number.

HOW TO PLAY:
    type guessed number to the console.
-----------------------------------------------------
""")
    
# this function takes the user input in integer
def userInput():
    user_input = int(input("guess: "))
    return user_input

# generating random number
randomNum = randint(1, 100)

instructions() 

while (guess != 0):

    user_input = userInput()
    if (user_input > randomNum):
        guess -= 1
        print("you guessed higher number")
        print(f"remaining gueses: {guess}\n")
    elif (user_input < randomNum):
        guess -= 1
        print("you guessed lower number")
        print(f"remaining gueses: {guess}\n")
    elif (user_input == randomNum):
        print(f"you guessed the correct number: {randomNum}\n")
        print("Do you want to play again,\ntype y-yes\nn-no")     
        choice = input(":")

        if (choice.lower() == "y"):
            randomNum = randint(1, 100)
            guess = 10
        else:
            break

    if (guess == 0):
        print(f"the correct guess was {randomNum}\n")
        print("Do you want to play again,\ntype y-yes\nn-no")     
        choice = input(":")

        if (choice.lower() == "y"):
            randomNum = randint(1, 100)
            guess = 10
        else:
            break

print("\n\nHope you enjoyed the game.\nPlay again sometimes.")
    