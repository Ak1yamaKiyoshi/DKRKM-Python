
from tkinter import *
from math import *

root = Tk()
root.geometry("310x320+500+100")
root.title("Individual Task")
author = Label(root, text="Kolosov Igor, CS-21-1")

def calculation(event):
    global a,b,c,d
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    d = float(entry_d.get())
    
input_data_frame = LabelFrame(root, text="Input Data")
label_a = Label(input_data_frame, text="a")
label_b = Label(input_data_frame, text="b")
label_c = Label(input_data_frame, text="c")
label_d = Label(input_data_frame, text="d")
entry_a = Entry(input_data_frame, width=5)
entry_b = Entry(input_data_frame, width=5)
entry_c = Entry(input_data_frame, width=5)
entry_d = Entry(input_data_frame, width=5)
button_1 = Button(root, width="15", text="Calculate")
button_1.bind("<Button-1>", calculation)
    
input_data_frame.pack(padx=10, pady=10, fill=BOTH)
label_a.pack(side=LEFT, padx=10, pady=10)
entry_a.pack(side=LEFT)
label_b.pack(side=LEFT, padx=10, pady=10)
entry_b.pack(side=LEFT)
label_c.pack(side=LEFT, padx=10, pady=10)
entry_c.pack(side=LEFT)
label_d.pack(side=LEFT, padx=10, pady=10)
entry_d.pack(side=LEFT)
    
output_data_frame = LabelFrame(root, text="Input Data")
Answer_Result_1 = Label(output_data_frame)
Answer_Result_2 = Label(output_data_frame)
Answer_Result_3 = Label(output_data_frame)
Answer_Result_4 = Label(output_data_frame)
Answer_Result_5 = Label(output_data_frame)
Answer_Max = Label(output_data_frame)
Answer_Min = Label(output_data_frame)



Result_list = [Result_1, Result_2, Result_3, Result_4, Result_5]
Answer_Result_1["text"] = "Result_1 = %s" % round(Result_list[0], 2)
Answer_Result_2["text"] = "Result_2 = %s" % round(Result_list[1], 2)
Answer_Result_3["text"] = "Result_3 = %s" % round(Result_list[2], 2)
Answer_Result_4["text"] = "Result_4 = %s" % round(Result_list[3], 2)
Answer_Result_5["text"] = "Result_5 = %s" % round(Result_list[4], 2)
Answer_Max["text"] = "Максимальне значення: Max = %s" % round(max(Result_list), 2)
Answer_Min["text"] = "Мінімальне значення: Min = %s" % round(min(Result_list), 2)
button_1.pack()

Result_1 = a
Result_2 = b
Result_3 = c
Result_4 = a
Result_5 = d

output_data_frame.pack(padx=10, pady=10, fill=BOTH)
Answer_Result_1.pack(anchor=W, padx=10)
Answer_Result_2.pack(anchor=W, padx=10)
Answer_Result_3.pack(anchor=W, padx=10)
Answer_Result_4.pack(anchor=W, padx=10)
Answer_Result_5.pack(anchor=W, padx=10)
Answer_Max.pack(anchor=W, padx=10)
Answer_Min.pack(anchor=W, padx=10)

author.pack()

root.mainloop()



