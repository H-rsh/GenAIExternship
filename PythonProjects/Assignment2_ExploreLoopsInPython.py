# Assignment: Explore Loops in Python
# By: Harsh Chavva

# Task 1 - Counting Down with Loops
print("Please enter a whole number you want to count down from: ")
userNum = input()
try:
    num = int(userNum)
    while num > 0:
        print(num, end = " ")
        num -= 1
    print("Blast Off! 🚀")
except ValueError:
    print("Sorry, that is not allowed. Please enter a whole number next time.")

print()

# Task 2 - Multiplication Table with for Loops
try: # Works for both whole numbers and numbers with decimals
    num2 = float(input("Please tell me which number you'd like to see the multiples of: ")) 
    for count in range (1, 11):
        print(num2, "x", count, "=", (num2 * count))
except ValueError:
    print("Sorry, that is not allowed. Please enter a number next time.")

print()

# Task 3 - Find the Factorial
try:
    num3 = int(input("Please tell me which number you'd like to see the factorial of: "))
    f = num3
    for count in range (1, num3):
        f *= count
    print("The factorial of", num3, "is", f)
except ValueError:
    print("Sorry, that is not allowed. Please enter a whole number next time.")