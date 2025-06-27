# Assignment: Exploring String Methods
# By: Harsh Chavva

# Task 1 - String Slicing and Indexing
sen = "Python is amazing!"
print("First word:", sen[:6])
print("Amazing part:", sen[10:17])
print("Reversed string:", sen[::-1])

print()

# Task 2 - String Methods
world = " hello, python world! "
world = world.strip()
world = world.capitalize()
world = world.replace("world", "universe")
world = world.upper()
print(world)
print()

# Task 3 - Check for Palindromes
print("Enter a word to check if it's a palindrome: ")
user = input()
check = user[::-1]
if user == check:
    print("Yes, '" + user + "' is a palindrome!") # so there is no space between the user variable and the quotation marks ('') on either end
else:
    print("Sorry, no", user, "is just a regular word.")