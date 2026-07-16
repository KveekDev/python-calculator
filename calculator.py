import os
os.system('cls' if os.name == 'nt' else 'clear')
import math
import time

history = []
calculator_active = "yes"

def color_red(text):
    RED = "\033[31m"
    RESET = "\033[0m"
    return f"{RED}{text}{RESET}"
def color_yellow(text):
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    return f"{YELLOW}{text}{RESET}"
def hello():
    print("\n Welcome to the Python Calculator!")
    print("You can exit the program by entering 'q' instead of the first number.")
    print("To find the square root, use 'root'. For power, use '**'.")
    print("---")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
def power(a, b):
    return a ** b 
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
hello()
while calculator_active == "yes":
    while True: # No. 1
        try:
            first_input = input("Enter the first number: ").strip().lower()
            if first_input == "q":
                print("\n Exiting the program as requested...")
                calculator_active = "no"
                break
            num1 = int(first_input)
            break
        except ValueError:
            print(color_red("Hey! Enter a valid first number!"))
        if calculator_active == "no":
            break
    if calculator_active == "no":
        break
    while True: # No. 2 
        calculator_action = input("Enter an operation: ").strip()
        if calculator_action in {"-", "/", ":", "+", "*", "root", "**"}:
            break
        else:
            print(color_red("Invalid operation! Please enter a valid one."))
    if calculator_action != "root":
        while True: # No. 3
            try:
                num2 = int(input("Enter the second number: ").strip())
                break
            except ValueError:
                print(color_red("Hey! Enter a valid second number!"))
    result = None
    final_result = None

    if calculator_action == "+":
        result = add(num1, num2)
        final_result = f"{num1} + {num2} = {result}"
    elif calculator_action == "-":
        result = subtract(num1, num2)
        final_result = f"{num1} - {num2} = {result}"
    elif calculator_action == "*":
        result = multiply(num1, num2)
        final_result = f"{num1} * {num2} = {result}"
    elif calculator_action == "/":
        try:
            result = divide(num1, num2)
            final_result = f"{num1} : {num2} = {result}"
        except ZeroDivisionError: 
            print(f"{color_red('Hey, division by zero is not allowed!')}\n")
            time.sleep(1)
            print(f"{color_yellow('Let\'s try again...')}\n")
            continue 
    elif calculator_action == ":":
        try:
            result = divide(num1, num2)
            final_result = f"{num1} : {num2} = {result}"
        except ZeroDivisionError: 
            print(f"{color_red('Hey, division by zero is not allowed!')}\n")
            time.sleep(1)
            print(f"{color_yellow('Let\'s try again...')}\n")
            continue 
    elif calculator_action == "**":
        result = power(num1, num2)
        final_result = f"{num1} ** {num2} = {result}"
    elif calculator_action == "root":
        try:
            result = square_root(num1)
            final_result = f"root({num1}) = {result}"
        except ValueError:
            print(color_red("Hey! Cannot find the square root of a negative number!"))
            time.sleep(1)
            print(f"{color_yellow('Let\'s try again...')}\n")
            continue 
    if final_result is not None:
        print("\n Result:", result)
        history.append(final_result)

    choice = input("\n Do you want to continue? (yes/no): ").strip().lower()
    if choice == "no":
        calculator_active = "no"

for i in range(1, 4):
    dots = "." * i
    print(f"\r{color_yellow('Stopping the calculator')}{color_yellow(dots)}", end="", flush=True)
    time.sleep(1.2)
print("\n")

if len(history) > 0:
    for i in range(len(history)):
        print(f"Operation #{i + 1} ──> {history[i]}")
else:
    print("You closed the calculator without performing any calculations.")
