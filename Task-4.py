import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")

    elif user in choices:
        print("Computer Wins!")

    else:
        print("Invalid choice!")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break