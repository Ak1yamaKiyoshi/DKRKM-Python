from math import *

def script_1(x, a, c):
    print("script_1")
    print("x < 5, c ≠ 0")
    f = (-(a*x**2)-b)
    return round(f, 3)
def script_2(x, a):
    print("script_2")
    print("x > 5, c = 0")
    f = (x - a) / x
    return f
def script_3(x, c):
    print("script_3")
    f = -x / c
    return f

x = float(input("Присвоїти значення аргумету x: "))
a = float(input("Присвоїти значення аргумету a: "))
b = float(input("Присвоїти значення аргумету b: "))
c = float(input("Присвоїти значення аргумету c: "))

if x < 5 and c != 0:
    F = script_1(x, a, b)
elif x > 5 and c == 0:
    F = script_2(x, a)
else:
    F = script_3(x, c)
print("F (%s, %s %s, %s) = %s" % (x, a, b, c, F))


