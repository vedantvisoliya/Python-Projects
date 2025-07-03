# Python Quiz Game

questions = (
    "How many elements are there in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abudant gas in the Earth's atmosphere?: ",
    "How many bones are there in the adult human body?: ",
    "Which planet in the solar system is the hottest?: ",
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
)

answers = (
    "C",
    "D",
    "A",
    "A",
    "B",
)

guesses = []
score = 0
questions_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[questions_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    if (guess == answers[questions_num]):
        print("CORRECT!")
        guesses.append(guess)
        score += 1
    else:
        print(f"{answers[questions_num]} is the correct answer.")
        guesses.append(guess)
    questions_num += 1

print("--------------------")
print("       RESULTS      ")
print("--------------------")

print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")

print()

print("guess  :", end=" ")
for guess in guesses:
    print(guess, end=" ")

print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")