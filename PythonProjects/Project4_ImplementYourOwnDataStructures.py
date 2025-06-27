# Project: Implement Your own Data Structures
# By: Harsh Chavva

print("Welcome to the Inventory Manager!")

# Step 1: Create the Inventory
inventory = {}

while True:
    try:
        num_items = int(input("How many items would you like to start your inventory with: "))
        break
    except ValueError:
        print("Not allowed, please enter a whole number.")

for i in range(num_items):
    item = input("Enter the item's name: ").lower()
    while True:
        try:
            quantity = int(input(f"Enter the quantity of {item}: "))
            break
        except ValueError:
            print("Not allowed, please enter a whole number for quantity.")

    while True:
        try:
            price = float(input(f"Enter the price of {item}: $"))
            break
        except ValueError:
            print("Not allowed, please enter a number for price.")

    inventory[item] = (quantity, price)

# Display Current Inventory
print("\nCurrent inventory:")
for item, (quantity, price) in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price:0.2f}")

# Step 2: Menu to Add, Delete, or Update Items
while True:
    print("\nChoose an action: Add / Delete / Update / Done")
    action = input("What would you like to do? ").lower()

    if action == "add":
        item = input("Enter the new item's name: ").lower()
        while True:
            try:
                quantity = int(input(f"Enter the quantity of {item}: "))
                break
            except ValueError:
                print("Not allowed, please enter a whole number for quantity.")
        while True:
            try:
                price = float(input(f"Enter the price of {item}: $"))
                break
            except ValueError:
                print("Not allowed, please enter a number for price.")
        inventory[item] = (quantity, price)
        print(f"{item} added successfully.")

    elif action == "delete":
        item = input("Enter the item's name to delete: ").lower()
        if item in inventory:
            inventory.pop(item)
            print(f"{item} deleted successfully.")
        else:
            print(f"{item} not found in inventory.")

    elif action == "update":
        item = input("Enter the item's name to update: ").lower()
        if item in inventory:
            while True:
                try:
                    quantity = int(input(f"Enter the new quantity of {item}: "))
                    break
                except ValueError:
                    print("Not allowed, please enter a whole number for quantity.")
            while True:
                try:
                    price = float(input(f"Enter the new price of {item}: $"))
                    break
                except ValueError:
                    print("Not allowed, please enter a valid number for price.")
            inventory[item] = (quantity, price)
            print(f"{item} updated successfully.")
        else:
            print(f"{item} not found in inventory.")

    elif action == "done":
        break
    else:
        print("Not allowed, please enter Add, Delete, Update, or Done.")

# Step 3: Display Updated Inventory and Total Value
print("\nUpdated inventory:")
total = 0
for item, (quantity, price) in inventory.items():
    total += quantity * price
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price:0.2f}")

# Step 4: Show Total Value
print(f"Total value of inventory: ${total:0.2f}")