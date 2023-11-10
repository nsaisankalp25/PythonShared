import tkinter as tk
import checker
window = tk.Tk()
window.title("My first Pass checker")
window.geometry("500x500")
window.config(bg = "blue")

def submit_func():
    password_user = enter.get()
    print(password_user)
    
    results = checker.password_judgement(password_user)
    score = results[0]
    dict_results = results[1]

    res_win = tk.Tk()
    res_win.title("RESULTS/ANALYSIS")
    res_win.geometry("500x500")
    res_win.config(bg = 'black')

    length_l = tk.Label(res_win, text = 'Length', font = ("calibri", 14), fg = 'white')
    length_l.place(x = 50, y = 50)

    case_l = tk.Label(res_win, text = 'Case', font = ("calibri", 14), fg = 'white')
    case_l.place(x = 50, y = 100)

    nums_l = tk.Label(res_win, text = 'Numers', font = ("calibri", 14), fg = 'white')
    nums_l.place(x = 50, y = 150)

    Spl_l = tk.Label(res_win, text = 'Spl.Chars', font = ("calibri", 14), fg = 'white')
    Spl_l.place(x = 50, y = 200)

    Space_l = tk.Label(res_win, text = 'Spaces', font = ("calibri", 14), fg = 'white')
    Space_l.place(x = 50, y = 250)

    score_l = tk.Label(res_win, text = f'SCORE {score}%', font = ("calibri", 14), fg = 'yellow')
    score_l.place(x = 50, y = 300)

    #{'length':, 'spl.char':, 'Upper':, 'Lower':, 'Num':, "no_space":}
    if dict_results['length'] == True:
        length_l.config(text = 'LENGTH - PASS', fg = 'green')
    else:
        length_l.config(text = 'LENGTH - FAIL', fg = 'red')

    if dict_results['spl.char'] == True:
        Spl_l.config(text = 'SPL CHARS - PASS', fg = 'green')
    else:
        Spl_l.config(text = 'SPL CHARS - FAIL', fg = 'red')

    print(dict_results)
    if dict_results['Upper'] == True and dict_results["Lower"] == True:
        case_l.config(text = 'CASE - PASS', fg = 'green')
    else:
        case_l.config(text = 'CASE - FAIL', fg = 'red')

    if dict_results['Num'] == True:
        nums_l.config(text = 'NUMBERS - PASS', fg = 'green')
    else:
        nums_l.config(text = 'NUMBERS - FAIL', fg = 'red')

    if dict_results['no_space'] == True:
        Space_l.config(text = 'NO SPACE - PASS', fg = 'green')
    else:
        Space_l.config(text = 'NO SPACE - FAIL', fg = 'red')


    for i in res_win.winfo_children():
        i.config(bg = 'black')

label1 = tk.Label(window, text = "Enter your password",font = ("Berlin Sans FB",30 ), fg = "Red", bg = "blue")
label1.place(x = 100, y = 100)

enter = tk.Entry(window, bg = "White", fg = "Black", font = ("Berlin Sans FB", 20))
enter.place(x = 100, y = 200)

sub = tk.Button(window, text ="Submit", font = ("Berlin Sans FB", 15), 
                bg = "Black", fg = "White", command = submit_func)
sub.place(x = 200, y = 300)

window.mainloop()