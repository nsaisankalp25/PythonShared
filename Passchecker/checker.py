def password_judgement(password):
    score = 1
    score3 = {'length':False, 'spl.char':False, 'Upper':False, 'Lower':False, 'Num':False, "no_space":True}
    if len(password) >= 8:
        score += 1
        score3["length"] = True

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
        score += 0.5
        score3["Upper"] = True

    if v == True:
        score += 0.5
        score3["Lower"] = True

    if password.isalnum() != True:
        score += 1


    S = False
    for i in password:
        if i == " ":
            break
        elif i in "~`!@#$%^&*()_-+=}]|\"':;?/>.<,":
            S = True
            score += 1  
            score3["spl.char"] = True
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

    if b != False:
        score += 1
        score3["Num"] = True

    for i in password:
        if i.isspace() == True:
            score3["no_space"] = False
            score -= 1 
            break
        else:
            print("SPACE COND.FAILED")


    final = round((score/6)*100,2)
    return (final,score3)
   


