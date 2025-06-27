# Assignment: Check your Knowledge on Errors
# By: Harsh Chavva

# Task 1 - Understanding Python Exceptions
try:
    num = int(input("Enter a number you'd like to see 100 divided by: "))
    print("100 divided by", num, "is", (100 / num))
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Sorry, words aren't allowed. Please only enter valid numbers.")

print("")

# Task 2 - Types of Exceptions
    # IndexError Example
try:
    myList = [3, 2, 1]
    print(myList[10])  # This will cause IndexError: index 10 does not exist
except IndexError:
    print("IndexError occurred! List index out of range.")

    # KeyError Example
try:
    myDict = {"date": 1, "blueberry": 2}
    print(myDict["banana"])  # Key "banana" doesn't exist
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

    # TypeError Example
try:
    result = "Age: " + 23  # You can't add a string and an integer
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

print("")

# Task 3 - Using try...except...else...finally
try:
    num = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num / num2
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")