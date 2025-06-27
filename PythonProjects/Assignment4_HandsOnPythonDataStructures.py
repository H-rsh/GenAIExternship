# Assignment: Hands on Python Data Structures
# By: Harsh Chavva

# Task 1 - Working with Lists
fruits = ['blueberry', 'date', 'apple', 'strawberry', 'cherry', 'banana']
print("Original list:", fruits)
fruits.append("fig")
print("After adding a fruit:", fruits)
fruits.remove("banana")
print("After removing a fruit:", fruits)
print("Reversed list:", fruits[::-1])

print()

# Task 2 - Exploring Dictionaries
diction = {"name": "Harsh", 
           "age": 23, 
           "city": "Frisco"}
diction["favorite color"] = "cyan"
diction.update({"city": "New York"})

print("Keys: ", end = "")
i = 0
for k in diction:
    print(k, end = "")
    if i < len(diction) - 1:
        print(", ", end = "")
    i += 1
print()

print("Values: ", end = "")
i = 0
for v in diction:
    print(diction[v], end = "")
    if i < len(diction) - 1:
        print(", ", end = "")
    i += 1

print()

# Task 3 - Using Tuples
aboutMe = ("Treasure Planet", "Hard Times", "The Mysterious Bendict Society")
print("Favorite things:", aboutMe)
try:
    aboutMe[0]= "Kung Fu Panda"
except TypeError: # Since the above staement is not allowed, this allows my ide to print the below message instead of having an error pop up
    print("Oops! Tuples cannot be changed.")
print("Length of tuple:", len(aboutMe))