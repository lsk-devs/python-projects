import os
from time import sleep

books = []


def library_manager():
    max_choices = ["1", "2", "3", "4", "5", "6"]

    blacklist = [
        "@", "#", "$", "%", "&", "*", "!", "?",
        "/", "\\", "|", "=", "+", "<", ">",
        "{", "}", "[", "]", "(", ")", ";", ":"
    ]

    while True:
        print("""
            ========================================
                📚 PERSONAL LIBRARY 📚
            ========================================

                [1] Add a book
                [2] Show books
                [3] Search for a book
                [4] Remove a book
                [5] Number of books
                [6] Quit

            ========================================
            """)

        print()
        choice = input(">> ")

        if choice not in max_choices:
            print("❌ Invalid choice.")
            print("Please choose one of the following options: [1], [2], [3], [4], [5], [6]")
            print()
            input("Press Enter to return to the menu...")
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            continue

        if choice == max_choices[0]:
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)

            while True:
                print("📖 Enter the book title:")
                book_title = input(">> ")

                invalid = False

                for character in book_title:
                    if character in blacklist:
                        print("❌ Invalid title (special characters are not allowed).")
                        input("Press Enter to try again...")
                        os.system("cls" if os.name == "nt" else "clear")
                        invalid = True
                        break

                if invalid:
                    continue

                if book_title.isdigit():
                    print("❌ Invalid title.")
                    input("Press Enter to try again...")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue

                books.append(book_title)
                print("✅ Book added successfully!")
                print()
                input("Press Enter to return to the menu...")
                os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                break


if __name__ == "__main__":
    library_manager()