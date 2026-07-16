import os
from time import sleep

saved_number = None
YES_NO_CHOICES = ["y", "n"]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def clear_and_sleep():
    sleep(0.5)
    clear()

def error_manager():
    print("❌ Invalid choice.")
    input("Press any key to return to the main menu...")

def ask_to_store(result):
    global saved_number

    while True:
        clear()
        store_choice = input(
            f"Do you want to store your result? (your result is: {result}) "
            "You can use it for other operations. y/n: "
        ).lower().strip()

        if store_choice == "":
            continue

        if store_choice not in YES_NO_CHOICES:
            print("❌ Please enter y or n.")
            sleep(1)
            continue

        if store_choice == "y":
            saved_number = result
            print("\nResult saved!")
            sleep(1)
            return

        print("You will be moved to the main menu soon..")
        sleep(1)
        return

def get_number(prompt, allow_saved=True):
    if allow_saved and saved_number is not None:
        use_saved = input(
            f"\nWe detected that you have a saved result ({saved_number}). Do you want to use it? y/n: "
        ).lower()

        if use_saved == "y":
            return saved_number

    while True:
        try:
            number = input(prompt)

            if not number:
                return None

            return float(number)

        except ValueError:
            print("❌ Invalid number. Please enter a valid number.")
            sleep(1)


def get_two_numbers(operation_name):
    while True:
        clear()
        print(f"\n━━━━━━━━━━ 🟡 {operation_name.upper()} ━━━━━━━━━━")
        print(f"➜ Enter the two numbers for {operation_name}.\n")

        num1 = get_number("First number: ")

        if num1 is not None:
            break

    while True:
        num2 = get_number("Second number: ")

        if num2 is not None:
            break

        clear()
        print(f"\n━━━━━━━━━━ 🟡 {operation_name.upper()} ━━━━━━━━━━")
        print(f"➜ Enter the two numbers for {operation_name}.\n")
        print(f"First number: {num1}")

    return [num1, num2]

def calculate(operation_name, symbol, operation):
    nums = get_two_numbers(operation_name)
    result = operation(nums[0], nums[1])

    print("\n✅ Numbers registered.")
    print("🧮 Calculating result...\n")
    sleep(0.5)
    print(f"{nums[0]} {symbol} {nums[1]} = {result}")
    sleep(2)
    ask_to_store(result)

def addition():
    calculate("addition", "+", lambda a, b: a + b)

def substraction():
    calculate("substraction", "-", lambda a, b: a - b)

def multiplication():
    calculate("multiplication", "*", lambda a, b: a * b)

def division():
    print("\n━━━━━━━━━━ 🔵 DIVISION ━━━━━━━━━━")
    print("➜ Enter the dividend and the divisor.\n")

    num1 = get_number("Dividend: ")
    num2 = get_number("Divisor: ")

    if num2 == 0:
        print("❌ Division by zero is not allowed.")
        sleep(1)
        return

    result = num1 / num2

    print("\n✅ Numbers registered.")
    print("🧮 Calculating result...\n")
    sleep(0.5)
    print(f"{num1} / {num2} = {result}")
    sleep(2)
    ask_to_store(result)

def display_menu():
    print("""
========================================
             🧮 CALCULATOR 🧮
========================================
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
[5] Reset (saved number)
[6] Quit
========================================
""")

def quit():
    print("""
========================================
              👋 EXITING 👋
========================================

Thanks for using the Calculator!

See you next time!
========================================
""")

def main():
    global saved_number

    while True:
        clear_and_sleep()
        display_menu()
        choice = input(">> ")

        if not choice:
            continue

        elif choice == "1":
            clear_and_sleep()
            addition()

        elif choice == "2":
            clear_and_sleep()
            substraction()

        elif choice == "3":
            clear_and_sleep()
            multiplication()

        elif choice == "4":
            clear_and_sleep()
            division()

        elif choice == "5":
            clear_and_sleep()
            saved_number = None
            print("Saved number has been reset.")
            sleep(1)

        elif choice == "6":
            clear_and_sleep()
            quit()
            sleep(2)
            break

        else:
            clear_and_sleep()
            error_manager()

if __name__ == "__main__":
    main()