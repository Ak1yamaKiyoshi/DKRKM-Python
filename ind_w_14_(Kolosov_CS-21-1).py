from tkinter import *
from math import *

root = Tk()
root.title ("Виконання розрахунків")
#root.iconphoto (True, PhotoImage (file="img/fkrkm_dnu.png"))
root.geometry ("+500+200")
root.config (background="#313335")
root.resizable (False, False)

def calculation():
    V = float (entry_a.get())
    x = float (entry_b.get())
    Label(right_frame,
                text=f'Вихідні данні \n Індивідуальне завдання №14 \n Варіант {int(V)}',
                foreground="#bababa",
                background="#313335").grid (row=0, column=0, sticky=W)
    if x <= -3:
        Result_1["text"] = "x <= -3 = " + str(tan(V/x - V**x))
    if -3 < x < 0:
        Result_1["text"] = "-3 < x < 0 = " + str(abs((cos(V-x))/(1-x)))
    if 0 <= x <= 2:
        Result_1["text"] = "0 <= x <= 2 = " + str(sqrt(x**V + V**x))
    if x > 2:
        Result_1["text"] = "x > 2 = " + str(sin(2-V**log(x)))
def author():
    author_app = Label(root,
                        text="© Колосов І.Д. СS-21-1",
                        foreground="#3778f5",
                        background="#313335")
    author_app.grid(row=1, column=0, pady=10)


left_frame = LabelFrame(text="Вхідні данні",
                        foreground="#bababa",
                        background="#313335",
                        relief=RIDGE, )
label_a = Label(left_frame,
                     text="V",
                     foreground="#bababa",
                     background="#313335")
label_b = Label(left_frame,
                     text="x",
                     foreground="#bababa",
                     background="#313335")

entry_a = Entry(left_frame,
                 width=10,
                 foreground="#bababa",
                 background="#4e5254",
                 highlightthickness=1,
                 highlightbackground="#bababa",
                 highlightcolor="#3778f5",
                 insertbackground="#bababa",
                 relief=FLAT)
entry_b = Entry(left_frame,
                 width=10,
                 foreground="#bababa",
                 background="#4e5254",
                 highlightthickness=1,
                 highlightbackground="#bababa",
                 highlightcolor="#3778f5",
                 insertbackground="#bababa",
                 relief=FLAT)

button_1 = Button(left_frame,
                   text="Обчислити",
                   width=12,
                   foreground="#ffffff",
                   background="#365880",
                   activeforeground="#3778f5",
                   activebackground="#00293e",
                   relief=RIDGE,
                   command=calculation)
right_frame = Frame(root,
                     background="#313335",
                     relief=RIDGE)
Result_1 = Label(right_frame,
                  foreground="#bababa",
                  background="#313335")


left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N)
label_a.grid(row=0, column=0, pady=10, sticky=E)
label_b.grid(row=1, column=0, sticky=E)


entry_a.grid(row=0, column=1, padx=5)
entry_b.grid(row=1, column=1, padx=5)


button_1.grid(row=4, columnspan=2, padx=10, pady=10)

right_frame.grid(row=0, rowspan=2, column=1, padx=10, pady=10, sticky=N)

Result_1.grid(row=1, column=0, padx=10, sticky=W)



author()
root.mainloop()