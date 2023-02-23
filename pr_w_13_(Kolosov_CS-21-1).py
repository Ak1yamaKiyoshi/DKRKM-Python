from tkinter import *
from math import *

root = Tk()

root.title("Значення тригонометричних функцій")
# root.iconphoto(True, PhotoImage(file="img/fkrkm_dnu.png"))
root.geometry("380x200+500+100")
# root.resizable(False, False)

top_frame = LabelFrame(root, text="Вхідні данні")
label_1 = Label(top_frame, text="Укажіть градусну міру кута:")
entry_1 = Entry(top_frame, width=5)
button_1 = Button(top_frame, text="Обчислити", width=25)

top_frame.pack(padx=10, pady=10, fill=BOTH)
label_1.pack(side=LEFT, padx=10, pady=10)
entry_1.pack(side=LEFT)
button_1.pack(side=LEFT, padx=20)

bottom_frame = LabelFrame(root, text="Вихідні данні")
bottom_left_frame = Frame(bottom_frame)
bottom_middle_frame = Frame(bottom_frame)
bottom_right_frame = Frame(bottom_frame)
answer_deg_rad = Label(bottom_left_frame)
answer_sin = Label(bottom_middle_frame)
answer_cos = Label(bottom_middle_frame)
answer_tan = Label(bottom_right_frame)
answer_ctan = Label(bottom_right_frame)

bottom_frame.pack(padx=10, pady=10, fill=BOTH)
bottom_left_frame.pack(side=LEFT)
bottom_middle_frame.pack(side=LEFT)
bottom_right_frame.pack(side=LEFT)
answer_deg_rad.pack(anchor=W, padx=10)
answer_sin.pack(anchor=W, padx=10)
answer_cos. pack(anchor=W, padx=10)
answer_tan.pack(anchor=W, padx=10)
answer_ctan.pack(anchor=W, padx=10)

author = Label(root, text="© Колосов Ігор, CS-21-1")
author.pack()

def calculation(event):
    alpha_deg = float(entry_1.get())
    alpha_rad = radians(alpha_deg)

    sin_alpha = sin(alpha_rad)
    cos_alpha = cos(alpha_rad)
    tan_alpha = tan(alpha_rad)
    ctan_alpha = pow(tan_alpha, -1)

    answer_deg_rad["text"] = "%s = %s радіан" % (int(alpha_deg), round(alpha_rad, 3))
    answer_sin["text"] = "sin %s° = %s" % (int(alpha_deg), round(sin_alpha, 3))
    answer_cos["text"] = "cos %s° = %s" % (int(alpha_deg), round(cos_alpha, 3))
    answer_tan["text"] = "tg %s° = %s" % (int(alpha_deg), round(tan_alpha, 3))
    answer_ctan["text"] = "ctg %s° = %s" % (int(alpha_deg), round(ctan_alpha, 3))

button_1.bind("<Button-1>", calculation)

root.mainloop()
