import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *
import csv
import os


now_date = datetime.now()
last_century = now_date.year - 100

day_list = [i + 1 for i in range(31)]
month_dict = {"Січень": 1, "Лютий": 2, "Березень": 3, "Квітень": 4, "Травень": 5, "Червень": 6,
              "Липень": 7, "Сперпень": 8, "Вересень": 9, "Жовтень": 10, "Листопад": 11, "Грудень": 12}
year_list = [i + last_century for i in range(now_date.year - last_century + 1)]

group_name = ["БО","ЕП","КС","ПЗ","ТВ","ТО",]
group_year = [i for i in range(now_date.year - 3 - 2000, now_date.year + 1 - 2000)]

def process_data():
    a = entry_last_name.get()
    b = entry_first_name.get()
    c = entry_middle_name.get()
    d = combobox_day.get()
    e = combobox_month.get()
    f = combobox_day.get()
    g = entry_phone_number.get()
    h = entry_mail.get()
    k = combobox_gn.get()
    l = combobox_gy.get()
    m = combobox_num.get()

    with open("C:/Users/akiyama/Documents/(A) Projects/College/[00] CS/[00] Done/new_file.csv", "a+", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow([a, b, c, d, e, f, g, h, k, l, m])

    messagebox.showinfo("",f'Реєстрація студента {a} {b} {c}, Вас успішно зароеєстровано')

    entry_last_name.delete(0, END)
    entry_first_name.delete(0, END)
    entry_middle_name.delete(0, END)
    combobox_day.delete(0, END)
    combobox_month.delete(0, END)
    combobox_day.delete(0, END)
    entry_phone_number.delete(0, END)
    entry_mail.delete(0, END)
    combobox_gn.delete(0, END)
    combobox_gy.delete(0, END)
    combobox_num.delete(0, END)

def author():
    author_app = Label(root, text="Колосов Ігор CS-21-1")
    author_app.grid(row=3, column=1, columnspan=2)

def open_csv_file():
    os.startfile("C:/Users/akiyama/Documents/(A) Projects/College/[00] CS/[00] Done/new_file.csv")

root = Tk()
root.title("Реєстрація студента в єдиному реєстрі ФКРКМ ДНУ")
root.iconphoto(True, PhotoImage(file="C:/Users/akiyama/Documents/(A) Projects/College/[00] CS/[00] Done/logo_fkrkm_dnu_1.png"))
root.geometry("+300+100")
root.resizable(False, False)

canvas_logo = Canvas(root, width=300, height=300, highlightthickness=0)
canvas_logo.grid(row=0, rowspan=4, column=0)
logo_fkrkm_dnu = PhotoImage(file="C:/Users/akiyama/Documents/(A) Projects/College/[00] CS/[00] Done/logo_fkrkm_dnu_1.png")
img_1 = canvas_logo.create_image(0, 10, anchor=NW, image=logo_fkrkm_dnu)

frame_first_last_name = ttk.LabelFrame(root, text="Вкажіть Прізвище Ім'я та Побатькові ")
label_last_name = ttk.Label(frame_first_last_name, text="Прізвище")
label_first_name = ttk.Label(frame_first_last_name, text="Ім'я")
label_middle_name = ttk.Label(frame_first_last_name, text="по батькові")

entry_last_name = ttk.Entry(frame_first_last_name, width=25)
entry_first_name = ttk.Entry(frame_first_last_name, width=25)
entry_middle_name = ttk.Entry(frame_first_last_name, width=25)

frame_first_last_name.grid(row=0, column=1, sticky=NW, padx=10, ipadx=10, pady=10)
label_last_name.grid(row=0, column=0, sticky=W, padx=10)
label_first_name.grid(row=1, column=0, sticky=W, padx=10)
label_middle_name.grid(row=2, column=0, sticky=W, padx=10)
entry_last_name.grid(row=0, column=1, pady=10)
entry_first_name.grid(row=1, column=1, pady=10)
entry_middle_name.grid(row=2, column=1, pady=10)

frame_dmy = LabelFrame(root, text="Вкажіть день, місяць та рік свого народження")
label_day = Label(frame_dmy, text="День")
label_month = Label(frame_dmy, text="Місяць")
label_year = Label(frame_dmy, text="Рік")
combobox_day = ttk.Combobox(frame_dmy, width=10, values=day_list)
combobox_month = ttk.Combobox(
    frame_dmy, width=10, values=list(month_dict.keys()))
combobox_year = ttk.Combobox(frame_dmy, width=10, values=year_list)

frame_dmy.grid(row=0, column=2, sticky=NW, padx=10, ipadx=5, pady=10)
label_day.grid(row=0, column=0, sticky=W, padx=10)
label_month.grid(row=1, column=0, sticky=W, padx=10)
label_year.grid(row=2, column=0, sticky=W, padx=10)
combobox_day.grid(row=0, column=1, sticky=W, pady=10)
combobox_month.grid(row=1, column=1, sticky=W, pady=10)
combobox_year.grid(row=2, column=1, sticky=W, pady=10)

frame_contacts = ttk.LabelFrame(root, text="Вкажіть особисті данні:")
label_phone_number = ttk.Label(frame_contacts, text="номер телефону")
label_mail = ttk.Label(frame_contacts, text="mail")
entry_phone_number = ttk.Entry(frame_contacts, width=20)
entry_mail = ttk.Entry(frame_contacts, width=20)

frame_contacts.grid(row=1, column=1, sticky=NW, padx=10, ipadx=10)
label_phone_number.grid(row=0, column=0, sticky=E, padx=10)
label_mail.grid(row=1, column=0, sticky=E, padx=10)
entry_phone_number.grid(row=0, column=1, pady=10)
entry_mail.grid(row=1, column=1, pady=10)

frame_group = ttk.LabelFrame(root, text="Вкажіть номер групи:")
label_speciality = ttk.Label(frame_group, text="спеціальність")
label_of_admission = ttk.Label(frame_group, text="рік вступу")
label_num = ttk.Label(frame_group, text="номер")
combobox_gn = ttk.Combobox(frame_group, width=10, values=group_name)
combobox_gy = ttk.Combobox(frame_group, width=10, values=group_year)
combobox_num = ttk.Combobox(frame_group, width=10, values=["1", "2"])

frame_group.grid(row=1, rowspan=2, column=2, sticky=NW, padx=10, ipadx=5)
label_speciality.grid(row=0, column=0, sticky=W, padx=10)
label_of_admission.grid(row=1, column=0, sticky=W, padx=10)
label_num.grid(row=2, column=0, sticky=W, padx=10)
combobox_gn.grid(row=0, column=1, padx=20, pady=10)
combobox_gy.grid(row=1, column=1, padx=20, pady=10)
combobox_num.grid(row=2, column=1, padx=20, pady=10)

frame_buttons = Frame(root)
button_1 = Button(frame_buttons, width=20, text="Обробити дані", command=process_data)
button_2 = Button(frame_buttons, width=20, text="Показати у файлі", command=open_csv_file)

frame_buttons.grid(row=2, column=1, sticky=NW, pady=5)
button_1.grid(row=0, column=0, padx=10, pady=10)
button_2.grid(row=0, column=1, pady=10) 

author()
root.mainloop()