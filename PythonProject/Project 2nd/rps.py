import random
import os

choices = ["rock", "paper", "scissors"]


def play():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Rock / Paper / Scissors (q to quit): ").lower()

        if player_choice == "q":
            return False

        if player_choice not in choices:
            print("Invalid choice.")
            continue

        computer_choice = random.choice(choices)
        print("Computer:", computer_choice)

        if player_choice == computer_choice:
            print("Draw!")

        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            player_score += 1
            print("You win!")

        else:
            computer_score += 1
            print("You lose!")

        print("Score:", player_score, "-", computer_score)

        if player_score == 3:
            print("You won the game!")
            return True

        if computer_score == 3:
            print("You lost the game!")
            return True


while True:
    play()

    retry = input("Play again? (y/n): ").lower()

    if retry != "y":
        print("Program terminated.")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")