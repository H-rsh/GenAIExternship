# Project: Number Guessing Game
# By: Harsh Chavva

# Step 1: Generate a Random Number
import random
number_to_guess = random.randint(1, 100)

print() #To keep the output separate

# Step 2: Prompt the User for Guesses & Step 3: Count the Attempts
print("Try guessing a number between 1 and 100")
guess = False
count = 0
try:
    while guess != True:
        userNum = input("Enter your number guess: ")
        num = int(userNum)

        if num == number_to_guess:
            print("Congratulations!!! You guessed it!")
            print("Wow, you guessed it in", count, "attempts!")
            guess = True
        elif num > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        
        count += 1
        if count == 10:
            print("Sorry, too slow. Game over!!! Better luck next time!")
            guess = True
except ValueError:
    print("Sorry, that is not allowed. Please enter a whole number next time.")