# Assignment: Exploring Python Concepts
# By: Harsh Chavva

# Task 1 - Variables: Your First Python Intro
name = "Harsh"
age = 23
height = 5.11
print(f"Hi everyone, my name is {name}. I'm {height} feet tall, {age} years old and looking forward to getting to know all of you.")

print() #To keep the output separate

# Task 2 - Operators: Playing with Numbers
num1 = 5
num2 = 25
print("The sum of 5 and 25 is", num1 + num2)
print(f"The difference between 5 and 25 is {num1 - num2}. Personally, I prefer to start with the bigger number so I don't end up with a negative number, which in this case would mean 25 - 5 or {num2 - num1}")
print("If you multiply 5 and 25, you'd get", num1 * num2)
print(f"Finally, if you divide 5 by 25, you'd get {num1 / num2}. Although the more commonly seen division problem is 25 by 5, which equals {num2 / num1}")

print() #To keep the output separate

# Task 3 - Conditional Statements: The Number Checker
print("Please enter a number and I'll tell you if it's positive, negative, or zero:")
user = input()

try:
    number = float(user)
    if number > 0:
        print("This number is positive. Awesome!")
    elif number < 0:
        print("This number is negative. Better luck next time!")
    else:
        print("Zero it is. A perfect balance!")
except ValueError:
    print("Uh uh uh, that is not allowed. Please enter a number next time.")