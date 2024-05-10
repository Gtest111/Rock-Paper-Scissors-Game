import random

def get_winner(player, computer, cnt1, cnt2):
    if player == computer:
        return "It's a tie!", cnt1, cnt2
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        cnt1 += 1
        return "You win!", cnt1, cnt2
    else:
        cnt2 += 1
        return "Computer wins!", cnt1, cnt2

choices = ["rock", "paper", "scissors"]
cnt1 = 0
cnt2 = 0

while True:
    player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to end: ").lower()
    if player_choice == "quit":
        print("Final Scores:")
        print(f"CPU: {cnt2}")
        print(f"Player: {cnt1}")
        break
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chooses {computer_choice}")

    result, cnt1, cnt2 = get_winner(player_choice, computer_choice, cnt1, cnt2)
    print(result)
