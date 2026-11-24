import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

player = input("Choose rock, paper, or scissors: ").lower().strip()

if player not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
    exit()

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