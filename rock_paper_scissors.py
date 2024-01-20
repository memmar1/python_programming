import random

options = ("rock", "paper", "scissors")

while True:
    
    print("")
    print("PLEASE ENTER ANY ONE OF THE CHOICES: rock, paper, or scissors")
    player = 0
    while player not in options:
        player = input("ENTER YOUR CHOICE: ")

    computer = random.choice(options)
    print("COMPUTER'S CHOICE:", computer)

    if player == computer:
        print("It's a tie")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break

print("Thank you for playing")
