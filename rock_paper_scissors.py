
import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

print("Welcome to Rock Paper Scissors!")

while True:
    player = input("Choose rock, paper, scissors or quit: ").lower().strip()

    if player == "quit":
        break

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a draw!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You win!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")

print("\nThanks for playing!")
print(f"Final score: You {player_score} - Computer {computer_score}")