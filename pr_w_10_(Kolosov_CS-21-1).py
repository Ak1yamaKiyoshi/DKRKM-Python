from math import *

x = float(input("Присвоїти значення аргументу x: "))
a = float(input("Присвоїти значення аргументу a: "))
b = float(input("Присвоїти значення аргументу b: "))
c = float(input("Присвоїти значення аргументу c: "))

if x < 0 and a != 0:
    print(" x < 0, a != 0 ")
    F = (a * pow(x, 2) + b * x + c) / (2 * x - 5)
elif 0 <= x < 1:
    print(" 0 <= x < 1 ")
    F = pow(a * pow(x, c) - pow(4, b), 3 * a + c)
elif x >= 1 and b == 0:
    print("x >= 1, b = 0")
    F = (4 * x + a * c) / sqrt(pow(x, 3) + pow(3, a + 1))
elif x > 1 and a ==0: 
    print("x > 1, a ==0, b < 0, c != 0")
    F =  sqrt(pow(x, c) + pow(b, 2)) / (2 * pow(c, 3))
else:
    F = (a * x + c) * (b * c - c)

print(f'F({x}; {a}; {b}; {c} = {F})')