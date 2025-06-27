# Assignment: About Parameters of Functions
# By: Harsh Chavva

# Task 1 - Writing Functions
def add_numbers(num, num2):
    return num + num2
def greet_user(name):
    print(f"Hey, {name}! Welcome aboard.")

user = str(input("What is your name: "))
greet_user(user)
try:
    num1 = float(input("Enter the first number you'd like to add: "))
    num2 = float(input("Enter the second number you'd like to add: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")
except ValueError:
    print("Please enter valid numbers.")

# Task 2 - Using Default Parameters
animal_type = "dog"
def describe_pet(pet_name, animal_type):
    print(f"I have a {animal_type} named {pet_name}.")
pName = str(input("What is your pet's name: "))
aType = str(input("What type of animal is your pet: "))
describe_pet(pName, aType)

# Task 3 - Functions with Variable Arguments
def make_sandwich(*ingre):
    print("Making a sandwich with the following ingredients: ")
    for item in ingre:
        print(f"- {item}")

# Task 4 - Understanding Recursion
x = int(input("Enter a number you'd like to know the factorial of: "))
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)
f = int(input("What number in the Fibonacci sequence would you like to calculate: "))
def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
print(f"Factorial of {x} is {factorial(x)}. The number {f} in the Fibonacci sequence is {fibonacci(f)}.")