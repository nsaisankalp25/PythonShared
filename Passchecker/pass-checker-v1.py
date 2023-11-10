password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
    print("Good strength", score)
else:
    print("Weak strength", score)

U = False
for i in password:
    if i.isupper() == True:
        U = True
        break
    else:
        continue

v = False
for j in password:
    if j.islower() == True:
        v = True
        break
    else:
        continue

if U == True:
    score += 1
    print("You have uppercase letters.")
else:
    print("You have no uppercase letters.")

if v == True:
    score += 1
    print("You have lowercase letters.")
else:
    print("You have no lower case letters.")

if password.isalnum() == True:
    print("Your password doesnt contain special characters.")
else:
    score += 1
    print("Your password contains special characters.")

S = False
for i in password:
    if i == " ":
        print("No spaces are required.")
        break
    elif i in "~`!@#$%^&*()_-+=}]|\"':;?/>.<,":
        S = True
        score += 1
        print("You have special characters")  
        break
    else:
        continue

b = False
for j in password:
    if j.isnumeric() == True:
        b = True
        break
    else:
        continue

if b == False:
    print("You do not have any numbers")
else:
    score += 1
    print("You have numbers")

print(f"Your final acceptability score is: {round((score/6)*100,2)}%")
    
















