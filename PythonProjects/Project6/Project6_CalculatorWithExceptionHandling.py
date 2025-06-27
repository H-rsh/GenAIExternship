# Project: Calculator with Exception Handling
# By: Harsh Chavva

import logging

# Step 4: Set up logging
logging.basicConfig(filename = 'error_log.txt', level = logging.ERROR)

print("Welcome to the Error-Free Calculator!")

# Step 1: Menu of Operations
while True:
    print("\nChoose an option (from 1 to 5):")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")
    print(" 5. Exit")
    try:
        opt = int(input("> "))
    except ValueError:
        print("Not allowed, please enter a whole number.")
        logging.error("ValueError occurred: Non-integer option entered.")
        continue
    
    # Step 2: Input Validation + Operations
    if opt in [1, 2, 3, 4]:
        try:
            print("To begin enter the two numbers you'd like to add, subtract, multiply or divide.")
            num = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError as e:
            print("Not allowed, please enter a whole number.")
            logging.error(f"ValueError occurred: {e}")
            continue

        try:
            if opt == 1:
                out = num + num2
                operation = "+"
            elif opt == 2:
                out = num - num2
                operation = "-"
            elif opt == 3:
                out = num * num2
                operation = "×"
        # Step 3: Division with Exception Handling
            elif opt == 4:
                out = num / num2
                operation = "/"
        except ZeroDivisionError as e: 
            print("Oops! Division by zero is not allowed.")
            logging.error(f"ZeroDivisionError occurred: {e}")
        else:
            print(f"{num} {operation} {num2} = {out}")
        finally:
            print("Your equation completed.")

    # Exit
    elif opt == 5:
        print("Bye, see you again later.")
        break
    else:
        print("Not allowed, please select from the options: 1, 2, 3, 4 or 5.")