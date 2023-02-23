from tkinter import *
from math import *

root = Tk()
root.title ("Виконання розрахунків")
#root.iconphoto (True, PhotoImage (file="img/fkrkm_dnu.png"))
root.geometry ("+500+200")
root.config (background="#313335")
#root.resizable (False, False)

def calculation():
    a = float (entry_a.get())
    b = float (entry_b.get())
    c = float (entry_c.get())
    d = float (entry_d.get())
    Label(right_frame,
                text="Вихідні данні:",
                foreground="#bababa",
                background="#313335").grid (row=0, column=0, sticky=W)
    Result_1["text"] = "Result_1 = " + str(pow(b - a * c, d))
    Result_2["text"] = "Result_2 = " + str(2 * (b - a) - c / sin(pi / 2))
    Result_3["text"] = "Result_3 = " + str(a * pi + c * b - 2 * d)
    Result_4["text"] = "Result_4 = " + str((a + c) * (b - d))
    Result_5["text"] = "Result 5 = " + str(pow(a + b, a - b))
    Result_6["text"] = "Result_6 = " + str(sqrt(pow(a - b, 2) + pow(c * d, 2)))
    Result_7["text"] = "Result_7 = " + str(3 * sqrt(pow(2 * a - 4 * b + c / 3 - d / 2, 2)) - a * b * c / 4)
    Result_8["text"] = "Result_8 = " + str((5 * a + 3 * b) / (2 * pi) - (a * c + b* d) / pow (3, c))
    Result_9["text"] = "Result_9 = " + str(sqrt (pow (7, a) + pow (4, b) + pow (3, c) + pow (5, d)) )
    Result_10["text"] = "Result_10 = " + str(3 * cos(pi) - 2 / pi + 2 * sin(pi/2))

def author():
    author_app = Label(root,
                        text="Колосов Ігор СS-21-1",
                        foreground="#3778f5",
                        background="#313335")
    author_app.grid(row=1, column=0, pady=10)


left_frame = LabelFrame(text="Вхідні данні",
                        foreground="#bababa",
                        background="#313335",
                        relief=RIDGE, )
label_a = Label(left_frame,
                     text="a",
                     foreground="#bababa",
                     background="#313335")
label_b = Label(left_frame,
                     text="b",
                     foreground="#bababa",
                     background="#313335")
label_c = Label(left_frame,
                     text="c",
                     foreground="#bababa",
                     background="#313335")
label_d = Label (left_frame,
                 text="d",
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
entry_c = Entry(left_frame,
                 width=10,
                 foreground="#bababa",
                 background="#4e5254",
                 highlightthickness=1,
                 highlightbackground="#bababa",
                 highlightcolor="#3778f5",
                 insertbackground="#bababa",
                 relief=FLAT)
entry_d = Entry(left_frame,
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
Result_2 = Label(right_frame,
                        foreground="#bababa",
                        background="#313335")
Result_3 = Label(right_frame,
                        foreground="#bababa",
                        background="#313335")
Result_4 = Label(right_frame,
                  foreground="#bababa",
                  background="#313335")
Result_5 = Label(right_frame,
                  foreground="#bababa",
                  background="#313335")
Result_6 = Label(right_frame,
                  foreground="#bababa",
                  background="#313335")
Result_7 = Label(right_frame,
                  foreground="#bababa",
                  background="#313335")
Result_8 = Label(right_frame,
                  foreground="#bababa",
                  background="#313335")
Result_9 = Label(right_frame,
                  foreground="#bababa",
                  background="#313335")
Result_10 = Label(right_frame,
                   foreground="#bababa",
                   background="#313335")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N)
label_a.grid(row=0, column=0, pady=10, sticky=E)
label_b.grid(row=1, column=0, sticky=E)
label_c.grid(row=2, column=0, pady=10, sticky=E)
label_d.grid(row=3, column=0, sticky=E)

entry_a.grid(row=0, column=1, padx=5)
entry_b.grid(row=1, column=1, padx=5)
entry_c.grid(row=2, column=1, padx=5)
entry_d.grid(row=3, column=1, padx=5)

button_1.grid(row=4, columnspan=2, padx=10, pady=10)

right_frame.grid(row=0, rowspan=2, column=1, padx=10, pady=10, sticky=N)

Result_1.grid(row=1, column=0, padx=10, sticky=W)
Result_2.grid(row=2, column=0, padx=10, sticky=W)
Result_3.grid(row=3, column=0, padx=10, sticky=W)
Result_4.grid(row=4, column=0, padx=10, sticky=W)
Result_5.grid(row=5, column=0, padx=10, sticky=W)
Result_6.grid(row=6, column=0, padx=10, sticky=W)
Result_7.grid(row=7, column=0, padx=10, sticky=W)
Result_8.grid(row=8, column=0, padx=10, sticky=W)
Result_9.grid(row=9, column=0, padx=10, sticky=W)
Result_10.grid(row=10, column=0, padx=10, sticky=W)

author()
root.mainloop()