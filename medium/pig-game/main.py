import random

print("-------------------------------")
print("|   Welcome to the PIG GAME!  |")
print("-------------------------------")

def roll():
    min_value = 1
    max_value = 6
    value = random.randint(min_value, max_value)
    return value

while True:
    try:
        players = int(input("Enter the number of players (2-4): "))
        if 2 <= players <= 4:
            break
        else:
            print("Enter a valid number of players")
    except Exception as e:
        print(e)

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for player_idx in range(players):
        current_score = 0
        print(f"\nPlayer {player_idx+1} Turn")
        print(f"Your Total Score: {players_score[player_idx]}\n")

        while True:
            user_choice = input("Do you want to roll the dice? (y/yes): ").lower()
            if (user_choice != 'y'):
                break

            rolled_num = roll()
            if rolled_num == 1:
                current_score = 0
                print("You rolled 1, now your turn is over.")
                break
            else:
                current_score += rolled_num
                print(f"You Rolled: {rolled_num}")
                print(f"Your Score: {players_score[player_idx] + current_score}")

        players_score[player_idx] += current_score

max_score_idx = players_score.index(max(players_score))
min_score_idx = players_score.index(min(players_score))
print(f"\nPlayer {max_score_idx+1} Won, with Score: {players_score[max_score_idx]}")
print(f"\nPlayer {max_score_idx+1} lose, with Score: {players_score[max_score_idx]}")