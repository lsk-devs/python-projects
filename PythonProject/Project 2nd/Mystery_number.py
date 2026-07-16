import random
import os
from time import sleep


def rules():
    print("""
            ========================================
                        📜 RULES 📜
            ========================================

            🎯 Goal:
            Find the secret number randomly
            chosen by the program.

            📌 How to play?

            - Enter a number.
            - The program will tell you:
                📈 Higher
                📉 Lower

            - Keep guessing until you find
            the secret number.

            🏆 The fewer attempts you use,
            the better your score!
            Note: The number of attempts is random.
            """)

    input("Press Enter to return to the menu...")
    os.system("cls" if os.name == "nt" else "clear")


def play():
    attempts = 0
    max_attempts = random.randint(3, 9)

    secret_number = random.randint(1, 100)

    while attempts < max_attempts:
        print("Remaining attempts:", max_attempts - attempts)
        player_guess = input("🔢 Enter a number: ")

        if not player_guess.isdigit():
            print()
            print("❌ Invalid input.")
            print()
            continue

        player_guess = int(player_guess)
        attempts += 1

        if player_guess > secret_number:
            print()
            print("📉 Lower")
            print()

        elif player_guess < secret_number:
            print()
            print("📈 Higher")
            print()

        else:
            print()
            print(f"🎉 Congratulations! You found the secret number in {attempts} attempts!")
            print()
            input("Press Enter to return to the menu...")
            break

    else:
        print()
        print("💀 You lost! The secret number was:", secret_number)
        print()
        input("Press Enter to return to the menu...")

    os.system("cls" if os.name == "nt" else "clear")


def quit_game():
    print("""
    ========================================
            👋 EXITING THE GAME 👋
    ========================================

    Thanks for playing Mystery Number!

    See you next time! 🎲
    ========================================
    """)


def main():
    while True:
        print("""
        ========================================
                🎲 MYSTERY NUMBER 🎲
        ========================================

        Welcome to Mystery Number!

        Your goal is to guess the
        randomly generated secret number.

        📈 Higher
        📉 Lower

        ========================================

        [1] Play
        [2] Rules
        [3] Quit

        ========================================
        """)

        choice = input(">> ")

        if choice not in ("1", "2", "3"):
            sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            print("❌ Invalid choice.")
            input("Press Enter to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            continue

        if choice == "1":
            play()
            continue

        if choice == "2":
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            rules()
            continue

        if choice == "3":
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            quit_game()
            sleep(2)
            break


if __name__ == "__main__":
    main()