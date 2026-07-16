import os
from time import sleep

saved_number = None


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def clear_and_wait():
    clear()
    sleep(1)


def error_message():
    print("❌ Invalid choice.")
    input("Press any key to go back...")


def small_error(message):
    print(f"❌ {message}")
    sleep(1)


def delete_last_line():
    print("\033[F\033[K", end="")


def ask_operator(operations_wl):
    while True:
        co = input("Enter the operator : ").strip().lower()

        if not co:
            delete_last_line()
            continue

        if co not in operations_wl:
            small_error("Invalid operator.")
            delete_last_line()
            delete_last_line()
            continue

        return co


def get_number(message):
    while True:
        number = input(message).strip()

        if not number:
            continue

        if number.lower() == "q":
            return "q"

        try:
            return float(number)

        except ValueError:
            small_error("Invalid number.")


def ask_yes_no(message):
    while True:
        choice = input(message).strip().lower()

        if not choice:
            continue

        if choice not in ["y", "n"]:
            small_error("Please enter y or n.")
            continue

        return choice


def ask_store(result):
    global saved_number

    while True:
        ask = input(
            "Do you want to save your result for another operation or not ? y/n "
        ).strip().lower()

        if not ask:
            continue

        if ask not in ["y", "n"]:
            small_error("Please enter y or n.")
            continue

        if ask == "y":
            saved_number = result
            print(
                f"Result : {result}, saved successfully, you will be able to use it."
            )
            sleep(1)
            clear_and_wait()

        else:
            print("You will be redirected to the calculator..")
            sleep(1)
            clear_and_wait()

        return


def percentage(n):
    result = (n[0] * n[1]) / 100
    return result


def division(n):
    result = n[0] / n[1]
    return result


def multiplication(n):
    result = n[0] * n[1]
    return result


def subtraction(n):
    result = n[0] - n[1]
    return result


def addition(n):
    result = sum(n)
    return result

def calculate(numbers, co):
    if len(numbers) < 2:
        small_error("You need two numbers to perform the operation.")
        return None

    if co == "/":
        if numbers[1] == 0:
            small_error("Cannot divide by zero.")
            return None

        return division(numbers)

    if co == "+":
        return addition(numbers)

    if co == "-":
        return subtraction(numbers)

    if co == "*" or co == "x":
        return multiplication(numbers)

    if co == "%":
        return percentage(numbers)

    return None


def quit_display():
    print("""
    ========================================
                👋 EXITING 👋
    ========================================

    Thanks for using calculator_v2!

    See you next time! 🎲
    ========================================

    """)


def menu_display():
    print("""
        ====================================
                    CALCULATOR V2
        ====================================
        [1] Start calculator
        [2] Quit
          
        ====================================
    """)


def calculator_display():
    print("""
        ====================================
                    CALCULATOR V2 
        ==================================== 
        
        Operations available : "+", "-", "x", "*", "/", "%"
        
        (q to quit)
          
        ====================================
    """)


def Calculator():
    operations_wl = ["+", "-", "x", "*", "/", "%"]

    while True:
        numbers = []

        calculator_display()
        print("")

        if saved_number is not None:
            print("")

            ask_sn = ask_yes_no(
                "We detected a saved number. Do you want to use it as first number ? y/n "
            )

            if ask_sn == "y":
                numbers.append(saved_number)
                print("First number registered successfully")
                print("")

            else:
                choice1 = get_number("Enter the first number : ")

                if choice1 == "q":
                    clear_and_wait()
                    break

                numbers.append(choice1)

                print("First number registered successfully")
                print("")

                ask_saved_second = ask_yes_no(
                    "Do you want to use the saved number as second number ? y/n "
                )

                if ask_saved_second == "y":
                    numbers.append(saved_number)

                    print("Second number registered successfully")
                    print("")

                else:
                    choice2 = get_number("Enter the 2nd number : ")

                    if choice2 == "q":
                        clear_and_wait()
                        continue

                    numbers.append(choice2)

                    print("Second number registered successfully")
                    print("")

        else:
            choice1 = get_number("Enter the first number : ")

            if choice1 == "q":
                clear_and_wait()
                break

            numbers.append(choice1)

            print("First number registered successfully")
            print("")

            choice2 = get_number("Enter the 2nd number : ")

            if choice2 == "q":
                continue

            numbers.append(choice2)

            print("Second number registered successfully")
            print("")

            co = ask_operator(operations_wl)

        result = calculate(numbers, co)

        if result is None:
            continue

        print("")
        print(f"The result is : {result}")

        sleep(3)

        clear_and_wait()

        ask_store(result)


def main():
    max_choice = ["1", "2"]

    while True:
        menu_display()

        choice = input(">> ").strip()

        if not choice:
            clear()
            continue

        if choice not in max_choice:
            error_message()
            clear()
            continue

        if choice == "1":
            clear_and_wait()
            Calculator()

        elif choice == "2":
            clear()
            quit_display()
            sleep(2)
            break


if __name__ == "__main__":
    main()