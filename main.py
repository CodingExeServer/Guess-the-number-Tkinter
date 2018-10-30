from tkinter import *
from tkinter import messagebox
import random
import sys

global number
number = random.randint(1, 101)

def start_game():
    try:
        number_user = input_num.get("1.0", END)
        if int(number_user) > number:
            information_l = Label(main, text="C'est moins", fg="white", bg="black", font=("Consolas", 18, "bold"))
            information_l.place(x=100, y=480)
        elif int(number_user) < number:
            information_l = Label(main, text="C'est plus", fg="white", bg="black", font=("Consolas", 18, "bold"))
            information_l.place(x=100, y=480)
        elif int(number_user) == number:
            information_l = Label(main, text=f"Tu as trouvé le nombre!!\n({number})", fg="white", bg="black", font=("Consolas", 18, "bold"))
            information_l.place(x=50, y=480)
    except Exception as e:
        messagebox.showerror("False number", "Tu n'as pas entré un nombre correcte")
        sys.exit(1)

main = Tk()
main.title("Guess The Number - Coding.exe")
main.configure(bg="black")
main.geometry(f"{450}x{650}")

title = Label(main, text="Entre un nombre entre\n1 et 100", fg="white", bg="black", font=("Consolas", 25, "bold"))
title.place(x=25, y=25)

contain = Frame(main, width=350, height=35)
contain.place(x=50, y=325)
input_num = Text(contain, font=("Consolas", 18, "bold"), fg="black", bg="grey", relief="flat")
input_num.place(x=0, y=0)


button_frame = Frame(main, width=250, height=35, bg="black")
button_frame.place(x=150, y=420)
new_game = Button(button_frame, font=("Consolas", 18, "bold"), fg="white", bg="grey", relief="flat", text="Proposer", command=start_game)
new_game.place(x=0, y=-5)
main.mainloop()
