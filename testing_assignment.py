import random

options = ("rock", "paper", "scissors")

def play_round():
    player = None
    while player not in options:
        player = input("ENTER YOUR CHOICE: ")

    computer = random.choice(options)
    print("COMPUTER'S CHOICE:", computer)

    if player == computer:
        return "It's a tie"
    elif (player == "paper" and computer == "rock") or \
         (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper"):
        return "You win"
    else:
        return "You lose"

def play_game():
    player_score = 0
    computer_score = 0

    for _ in range(3):  # Play three rounds
        result = play_round()
        print(result)

        if "win" in result:
            player_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Player Score: {player_score} | Computer Score: {computer_score}\n")

    if player_score > computer_score:
        print("Congratulations! You won the best of three.")
    elif player_score < computer_score:
        print("Sorry, you lost the best of three.")
    else:
        print("It's a tie in the best of three.")

if __name__ == "__main__":
    play_game()
