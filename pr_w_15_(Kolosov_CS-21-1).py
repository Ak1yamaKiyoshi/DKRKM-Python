from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as massagebox
from datetime import *

month_dict = {"Січень":1, "Лютий":2, "Березень":3, "Квітень":4, "Травень":5, "Червень":6, "Липень":7, "Серпень":8, "Вересень":9, "Жовтень":10, "Листопад":11, "Грудень":12}

now_date = datetime.now()
last_century = now_date.year - 100

day_list = [i + 1 for i in range(31)]
year_list = [i + last_century for i in range(now_date.year - last_century +1)]

def process_data():
    user_last_name = entry_last_name.get()
    user_first_name = entry_first_name.get()
    user_middle_name = entry_middle_name.get()
    day_of_birth = combobox_day.get()
    month_of_birth = month_dict[combobox_month.get()]
    year_of_birth = combobox_year.get()
    
    user_full_years = now_date.year - int(year_of_birth)
    user_full_months = now_date.month - month_of_birth
    user_full_days = now_date.day - int(day_of_birth)
    
    if user_full_years < 18:
        massagebox.showerror("",f'Обмеження за віком, ви не досягли повноліття. Повних років: {abs(user_full_years)} p.')
    elif user_full_years == 18:
        massagebox.showerror("",f'Обмеження за віком, До повноліття вам залишилося: \n місяців: {abs(user_full_months)} \n днів: {abs(user_full_days)}')
    elif user_full_years == 18 and user_full_months == 0 > user_full_days:
        massagebox.showerror("",f'Обмеження за віком, До повноліття вам залишилося: \n днів: {abs(user_full_days)}')
    else:
        massagebox.showinfo("",f'Ви повнолітня людина. Повних років: \n {abs(user_full_years)} p.' )
        info_lfm_name["text"] = user_last_name + " " + user_first_name + " " + user_middle_name + " повнолітній"
    
root = Tk()
root.title("ПР№ #14")
root.geometry("260x420+550+100")
root.resizable(False, False)

frame_first_last_name = ttk.LabelFrame(root, text="Введіть ПІБ")
label_last_name = ttk.Label(frame_first_last_name, text="Прізвище")
label_first_name = ttk.Label(frame_first_last_name, text="Ім'я")
label_middle_name = ttk.Label(frame_first_last_name, text="По батькові")
entry_last_name = ttk.Entry(frame_first_last_name, width=20)
entry_first_name = ttk.Entry(frame_first_last_name, width=20)
entry_middle_name = ttk.Entry(frame_first_last_name, width=20)

frame_first_last_name.grid(row=0, column=0, sticky=W, padx=10, ipadx=10, pady=10)
label_last_name.grid(row=0, column=0, sticky=W, padx=10)
label_first_name.grid(row=1, column=0, sticky=W, padx=10)
label_middle_name.grid(row=2, column=0, sticky=W, padx=10)
entry_last_name.grid(row=0, column=1, pady=10)
entry_first_name.grid(row=1, column=1, pady=10)
entry_middle_name.grid(row=2, column=1, pady=10)

frame_dmy = LabelFrame(root, text="Введіть дату народження")
label_day = Label(frame_dmy, text = "День")
label_month = Label(frame_dmy, text = "Місяць")
label_year = Label(frame_dmy, text = "Рік")
combobox_day = ttk.Combobox(frame_dmy, width=10, values=day_list)
combobox_month = ttk.Combobox(frame_dmy, width=10, values=list(month_dict.keys()))
combobox_year = ttk.Combobox(frame_dmy, width=10, values=year_list)

frame_dmy.grid(row=1, column=0, sticky=W, padx=10, ipadx=5, pady=10)
label_day.grid(row=0, column=0, sticky=W, padx=10)
label_month.grid(row=1, column=0, sticky=W, padx=10)
label_year.grid(row=2, column=0, sticky=W, padx=10)
combobox_day.grid(row=0, column=1, sticky=W, pady=10)
combobox_month.grid(row=1, column=1, sticky=W, pady=10)
combobox_year.grid(row=2, column=1, sticky=W, pady=10)

button_1 = Button(root, width=20, text="Calculate form", command=process_data)
button_1.grid(row=2, column=0, pady=10)

frame_info = Frame(root)
info_lfm_name = Label(frame_info)
author = Label(frame_info, text="Kolosov Igor, CS-21-1")
frame_info.grid(row=3, column=0)
info_lfm_name.grid(row=0, column=0)
author.grid(row=1, column=0)

root.mainloop()