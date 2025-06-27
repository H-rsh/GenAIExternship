# Project: Eligible Elector
# By: Harsh Chavva

# Step 1: Ask the User’s Age
age = input("How old are you? ") # Takes the number that the user inputs and then saves it into the age variable

print() #To keep the output separate

# Step 2: Decide the Eligibility
try:
    num = float(age) # Converts the age variable from a string to a float and saves it into the num variable
    if int(num) >= 18: # Converts it to an integer, and checks if the num variable is greater than or equal to 18
        print("Congratulations! You are eligible to vote. Go make a difference!")
    elif int(num) < 18: # Converts it to an integer, and checks if the age variable is less than 18
        print("Oops! You’re not eligible yet. But hey, only", round(18 - num), "more years to go!") # Makes sure the printed value is a whole number after rounding the result of the subtraction
except ValueError:
    print("Sorry, that is not allowed. Please enter a number next time.")