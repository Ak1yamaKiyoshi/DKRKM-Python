from pickletools import read_int4


login_reg = "student"
password_reg = "cs-21-1"
login = input("Укажіть логін: ")
password = input("Укажіть пароль: ")

while login != login_reg or password != password_reg:
    print("Або логін або пароль вказанно невірно, будь ласка спробуйте ще раз.")
    login = input("Укажіть логін: ")
    password = input("Укажіть пароль: ")
    
print("Авторизація пройшла успішно! \n")

a = []

for i in range(1, 11):
    k = int(input(f'Введіть {i}-й елемент: '))
    a.append(k)
    
print("a = ", a)

count_zero = a.count(0)
print("Кількість нульових значень: ", count_zero)

a.sort()
print("Сортування за зростанням: а = ", a)

max_a = max(a)
min_a = min(a)
print("Максимальне з введених: ", max_a)
print("Мінімальне з введених: ", min_a)

Average = sum(a) / len(a)
print("Середне арифметичне: ", Average)

Sum_dodat = 0
Dobutok_not_par = 1
for i in a:
    if i > 0:
        Sum_dodat += i
    if i % 2 != 0: 
        Dobutok_not_par *= i
        
print("Сумма додатних чисел: ",Sum_dodat)
print("Сумма непарних чисел: ",Dobutok_not_par)
