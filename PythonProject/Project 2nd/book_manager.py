import os
from time import sleep

books = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def is_valid_title(title):
    if len(title) == 0:
        return False

    for char in title:
        if not char.isalpha() and char != " ":
            return False

    return True


def add_book():
    while True:
        clear_screen()
        print("📖 Add a book")
        print("----------")
        title = input("Book title: ").strip()

        if not title:
            sleep(1)
            continue

        if not is_valid_title(title):
            print("❌ Invalid title.")
        elif title in books:
            print("❌ This book is already in the library.")
        else:
            books.append(title)
            print("✅ Book added: " + title)

        input("\nPress Enter to continue...")
        break


def show_books():
    clear_screen()
    print("📚 Book list")
    print("---------")

    if len(books) == 0:
        print("❌ No books saved yet.")
    else:
        sorted_books = sorted(books)
        for i in range(len(sorted_books)):
            print(str(i + 1) + ". " + sorted_books[i])

    input("\nPress Enter to continue...")


def search_book():
    while True:
        clear_screen()
        print("🔍 Search a book")
        print("-------------")
        keyword = input("Title or keyword: ").strip().lower()

        if not keyword:
            sleep(1)
            continue

        found = False
        for book in books:
            if keyword in book.lower():
                print("✅ Found: " + book)
                found = True

        if not found:
            print("❌ No book matches your search.")

        input("\nPress Enter to continue...")
        break


def remove_book():
    while True:
        clear_screen()
        print("🗑️ Remove a book")
        print("-------------")
        title = input("Title of the book to remove: ").strip()

        if not title:
            sleep(1)
            continue

        if not is_valid_title(title):
            print("❌ Invalid title.")
            input("\nPress Enter to continue...")
            break

        matches = []
        for book in books:
            if title.lower() in book.lower():
                matches.append(book)

        if len(matches) == 0:
            print("❌ This book was not found.")
            input("\nPress Enter to continue...")
            break

        print("")
        for i in range(len(matches)):
            print(str(i + 1) + ". " + matches[i])

        choice = input("\nEnter the number of the book to remove (or 0 to cancel): ").strip()

        if not choice.isdigit():
            print("❌ Invalid choice.")
            input("\nPress Enter to continue...")
            break

        choice = int(choice)

        if choice == 0:
            break

        if choice < 1 or choice > len(matches):
            print("❌ Invalid choice.")
            input("\nPress Enter to continue...")
            break

        selected_book = matches[choice - 1]

        while True:
            confirm = input("Are you sure you want to remove '" + selected_book + "'? (y/n): ").strip().lower()
            if confirm == "y" or confirm == "n":
                break
            print("❌ Please answer with y or n.")

        if confirm == "y":
            books.remove(selected_book)
            print("✅ Book removed.")
        else:
            print("❌ Cancelled.")

        input("\nPress Enter to continue...")
        break


def count_books():
    clear_screen()
    print("📊 Number of books")
    print("---------------")
    print("You have " + str(len(books)) + " book(s) in your library.")
    input("\nPress Enter to continue...")


def show_menu():
    clear_screen()
    print("""
        ========================================
                   📚 MY LIBRARY 📚
        ========================================
        [1] 📖 Add a book
        [2] 📚 Show all books
        [3] 🔍 Search a book
        [4] 🗑️ Remove a book
        [5] 📊 Count books
        [6] 🚪 Quit
        ========================================""")


def main():
    while True:
        show_menu()
        print("")
        choice = input(">> ").strip()

        if not choice:
            continue

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            count_books()
        elif choice == "6":
            clear_screen()
            sleep(1)
            print("""
                    ========================================
                                👋 EXITING 👋
                    ========================================

                    Thanks for using Book Manager!

                    See you next time! 
                    ========================================
                    """)
            sleep(2)
            break
        else:
            print("❌ Invalid option, choose a number between 1 and 6.")
            input("\nPress Enter to continue...")


if __name__ = "__main__":
    main()
