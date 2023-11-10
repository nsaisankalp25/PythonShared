from random import randrange, choice
import checker

def generate():
    pas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!#$%^&*()_+|}{:\"?><-=[]\;'/.,'}"
    pas1 = ""
    for i in range(randrange(8,15)):
        pas1 += choice(pas)
    return(pas1)

while True:
    passs_check = generate()
    if checker.password_judgement(passs_check)[0] == 100:
        print("\nThis is your password: ", passs_check,)
        break
    else:
        continue