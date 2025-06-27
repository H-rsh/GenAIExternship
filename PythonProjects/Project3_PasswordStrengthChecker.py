# Project: Password Strength Checker
# By: Harsh Chavva

print("Let's check the strength of your password out of ten")
while True:
    # Step 1: Input the Password
    print("Enter a password:")
    pas = input()

    check = []
    score = 0

    # Step 2: Evaluate the Password 
    if len(pas) >= 8:
        score += 2 # Each passed check adds two points, and since there are five checks, the total ends at ten if the user passes all of them
        len_size = True
    else:
        len_size = False
        check.append("at least 8 characters long")
    
    if any(w.isupper() for w in pas):
        found_upper = True
        score += 2
    else:
        found_upper = False
        check.append("at least one uppercase letter")
    
    if any(w.islower() for w in pas):
        found_lower = True
        score += 2
    else:
        found_lower = False
        check.append("at least one lowercase letter")
    
    if any(w.isdigit() for w in pas):
        found_number = True
        score += 2
    else:
        found_number = False
        check.append("at least one number")
    
    s = r"[@_!#$%^&*()<>?/\|}{~:]"
    if any(w in s for w in pas):
        found_special = True
        score += 2
    else:
        found_special = False
        check.append("at least one special character")
    
    # Step 3: Test with Different Passwords
    if len_size and found_upper and found_lower and found_number and found_special:
        print("Your password is strong! 💪")
        print("Your password's strength score is", score, "/ 10")
        break
    else:
        if len(check) == 1:
            result = check[0]
        elif len(check) == 2:
            result = " and ".join(check)
        else:
            result = ", ".join(check[:-1]) + ", and " + check[-1]
        
        print("Your password needs", result + ".")
        print("Password Strength Score:", score, "/ 10\n")