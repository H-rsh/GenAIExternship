# Project: About Menu
# By: Harsh Chavva

import turtle

# I'm making the functions before putting them altogether in a while loop at the end
# Step 2: Factorial Function
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1) # Returns the factorial of a number using recursion
# Step 3: Fibonacci Function
def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
# Step 4: Recursive Fractal Pattern (Bonus)
def drawFractal(branchN, angle, reduction):
    try:
        # Start new turtle session
        window = turtle.Screen()
        turt = turtle.Turtle()
        turt.left(90)
        turt.speed(0)

        def draw(branch, turt):
            if branch > 5: # If the branch is short enough (5 or less), the function stops — the recursion ends.
                turt.forward(branch)                # Draw the main trunk or branch
                turt.right(angle)                   # Turn right for one sub-branch
                draw(branch - reduction, turt)      # Recursively draw smaller branch
                turt.left(angle * 2)                # Turn left for the other sub-branch
                draw(branch - reduction, turt)      # Recursively draw that one
                turt.right(angle)                   # Reset angle to original direction
                turt.backward(branch)               # Move back to original position
        
        draw(branchN, turt)
        print("Enjoy your custom fractal tree drawing! Please close the window of the drawing to return to the menu.")
        window.mainloop()
        turtle.bye()  # Fully reset the turtle system so user can make another fractal drawing without having to restart the menu
    except turtle.Terminator:
        print("Turtle graphics was closed unexpectedly.")

print("Welcome to the Recursive Artistry Program!")

# Step 1: Menu of Recursive Functions
while True:
    print("\nChoose an option:")
    print(" 1. Calculate Factorial")
    print(" 2. Find Fibonacci")
    print(" 3. Draw a Recursive Fractal")
    print(" 4. Exit")
    try:
        opt = int(input("> "))
    except ValueError:
        print("Not allowed, please enter a whole number.")
        continue
    
    # Step 2: Factorial Function
    if opt == 1:
        try:
            x = int(input("Enter a number you'd like to know the factorial of: "))
            if x < 0:
                print("Please enter a positive integer.")
            else:
                print(f"The factorial of {x} is {factorial(x)}.")
        except ValueError:
            print("Not allowed, please enter a whole number.")
            
    # Step 3: Fibonacci Function
    elif opt == 2:
        try:
            f = int(input("What number in the Fibonacci sequence would you like to calculate: "))
            if x < 0:
                    print("Please enter a positive integer.")
            else:
                print(f"The number {f} in the Fibonacci sequence is {fibonacci(f)}.")
        except ValueError:
            print("Not allowed, please enter a whole number.")

    # Step 4: Recursive Fractal Pattern (Bonus)
    elif opt == 3:
        try:
            branchN = int(input("Enter the starting branch length (best between 80 – 130): "))
            angle = int(input("Enter the branch angle (best between 15 – 40 degrees): "))
            reduction = int(input("Enter how much shorter each branch gets (best between 10 – 25): "))
            
            # Range checks
            if branchN <= 0 or angle <= 0 or reduction <= 0:
                print("All values must be positive.")
                continue
            if branchN < reduction:
                print("Starting branch length must be greater than reduction.")
                continue
            if angle >= 90:
                print("Please enter a smaller angle (less than 90 degrees).")
                continue

            drawFractal(branchN, angle, reduction)
        except ValueError:
            print("Not allowed, please enter valid whole numbers for the length, angle, and reduction.")
    # Exit
    elif opt == 4:
        print("Bye, see you again later.")
        break
    else:
        print("Not allowed, please select from the options: 1, 2, 3, or 4.")