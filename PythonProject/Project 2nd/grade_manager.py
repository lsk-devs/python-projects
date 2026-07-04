import os
import statistics
from time import sleep

grades = []

def add_grade():
    print("Enter the grade you want to add:")
    grade_input = input(">> ")
    while True:
        if grade_input.isdigit():
            grade = int(grade_input)

            if 0 <= grade <= 20:
                grades.append(grade)
                print("Grade added successfully!")
                print()
                input("Press any key to return to the main menu...")
                os.system("cls" if os.name == "nt" else "clear")
                break

            else:
                sleep(0.5)
                print("Invalid grade. Please enter a number between 0 and 20.")
                print()
                input("Press any key to retry...")
                os.system("cls" if os.name == "nt" else "clear")
                continue

        else:
            sleep(0.5)
            print("Invalid grade. Please enter a number between 0 and 20.")
            print()
            input("Press any key to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            break

def show_grade():
    while True:
        if grades:
            os.system("cls" if os.name == "nt" else "clear")
            sleep(0.5)
            print("Saved grades:", grades)
            print()
            input("Press any key to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            break

        else:
            os.system("cls" if os.name == "nt" else "clear")
            sleep(0.5)
            print("No grades have been saved yet.")
            print()
            input("Press any key to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            break

def show_average():
    while True:
        if grades:
            os.system("cls" if os.name == "nt" else "clear")
            sleep(0.5)
            print("Average grade:", statistics.mean(grades))
            print()
            input("Press any key to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            break

        else:
            os.system("cls" if os.name == "nt" else "clear")
            sleep(0.5)
            print("No grades have been saved yet.")
            print()
            input("Press any key to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            break

def show_highest():
    while True:
        if grades:
            os.system("cls" if os.name == "nt" else "clear")
            sleep(0.5)
            print("Highest grade:", max(grades))
            print()
            input("Press any key to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            break

        else:
            os.system("cls" if os.name == "nt" else "clear")
            sleep(0.5)
            print("No grades have been saved yet.")
            print()
            input("Press any key to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            break

def main():
    max_choices = ["1", "2", "3", "4"]

    while True:
        print("""
        ========================================
                    📚 GRADE MANAGER
        ========================================

        [1] Add a grade
        [2] Show grades
        [3] Show average
        [4] Show highest grade

        ========================================
        """)

        choice = input(">> ")

        if choice not in max_choices:
            os.system("cls" if os.name == "nt" else "clear")
            print("You can only choose one of these options: [1], [2], [3], [4]")
            print()
            input("Press any key to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
            continue

        if choice == max_choices[0]:
            os.system("cls" if os.name == "nt" else "clear")
            add_grade()
            continue

        if choice == max_choices[1]:
            os.system("cls" if os.name == "nt" else "clear")
            show_grade()
            continue

        if choice == max_choices[2]:
            os.system("cls" if os.name == "nt" else "clear")
            show_average()
            continue

        if choice == max_choices[3]:
            os.system("cls" if os.name == "nt" else "clear")
            show_highest()
            continue


if __name__ == "__main__":
    main()
