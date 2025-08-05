import random

# variables
user_score = 0
bot_score = 0
round = 1

# Functions 

# this function prints the welcome message, rules and instruction.
def instructions():
    print("""
---------- WELCOME TO SNAKE WATER GUN GAME -----------
INSTRUCTIONS: 
    1. You will be playing against a bot
    2. Game will be of 5 rounds
    3. Who ever score 5 points first wins.
    4. SNAKE beats WATER
    5. WATER beats GUN
    6. GUN beats SNAKE

HOW TO PLAY:
    1. type 0 for SNAKE
    2. type 1 for WATER  
    3. type 2 for GUN
-----------------------------------------------------
""")

# this function takes the user choice until user enter the correct choice [0,1,2]
def userChoice():
    user_choice = int(input("Enter Your Choice: "))
    while(True):
        if (user_choice == 0):
            return user_choice
        elif (user_choice == 1):
            return user_choice
        elif (user_choice == 2):
            return user_choice
        else:
            print("Invalid Input! Please try again.")
            user_choice = int(input("Enter Your Choice: "))

# this function will generate random choice for the bot
def botChoice():
    bot_choice = random.randint(0,2)
    return bot_choice

# this function converts the user number choice into words for display.
def convertChoiceToName(choice):
    if (choice == 0):
        return "SNAKE"
    elif (choice == 1):
        return "WATER"
    elif (choice == 2):
        return "GUN"

# this is the interface of how the rounds will look like.
def interface(round, userChoice, botChoice):
    user_choice = convertChoiceToName(userChoice)
    bot_choice = convertChoiceToName(botChoice)
    print(f"""
---------- ROUND {round} ----------
     USER             BOT
    {user_choice}            {bot_choice}
-----------------------------
""")

# this is the game logic which decides who is going to win 
def gameLogic(userChoice, botChoice):
    # 0 - SNAKE
    # 1 - WATER
    # 2 - GUN

    global user_score, bot_score

    if (userChoice == 0 and botChoice == 1):
        user_score += 1
    elif (userChoice == 0 and botChoice == 2):
        bot_score += 1
    elif (userChoice == 1 and botChoice == 0):
        bot_score += 1
    elif (userChoice == 1 and botChoice == 2):
        user_score += 1
    elif (userChoice == 2 and botChoice == 0):
        user_score += 1
    elif (userChoice == 2 and botChoice == 1):
        bot_score += 1

# check if the user want to play the game again or not 
def playAgainPrompt():
    print("Do you want to play again?")
    choice = input("Type:\n'y' for yes\n'n' for no\n:")
    while(True):
        if (choice.lower() == 'y'):
            return True
        elif (choice.lower() == 'n'):
            return False
        else: 
            print("Invalid Input! Enter a valid input.")
            choice = input("Type:\n'y' for yes\n\'n' for no\n:")

# displays the score and declares the winner
def winCheck():
    if (user_score > bot_score):
        print(f"""
----------------------------
SCORE -> USER    -     BOT
           {user_score}           {bot_score}
    YOU WON THE GAME!!!
----------------------------
""")
    elif (user_score < bot_score):
        print(f"""
----------------------------
SCORE -> USER    -     BOT
           {user_score}           {bot_score}
SORRY! BETTER LUCK NEXT TIME
----------------------------
""")
    else:
        print(f"""
----------------------------
SCORE -> USER    -     BOT
           {user_score}           {bot_score}
    MATCH DRAW!!!
----------------------------
""")


# ------------------ from here the main game logic starts ---------------------

instructions()

while(round <= 5):
    # taking user choice
    user_choice = userChoice()
    # getting bot choice
    bot_choice = botChoice()

    # game logic 
    gameLogic(user_choice, bot_choice)

    # display the interface of the game
    interface(round, user_choice, bot_choice)

    # if round equals to 5
    if (round == 5):
        winCheck()
        play = playAgainPrompt()
        if (play):
            print("""
----------------------------
       GAME RESTARTED
----------------------------
""")
            round = 1
            user_score = 0
            bot_score = 0
            continue
        else:
            pass
    
    round += 1

print("\n\nHope you enjoyed the game.\nPlay again sometimes.")