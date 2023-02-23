import math
from math import sqrt

print("Індивідуальне завдання №9")

j = float(input("Задати значення пареметру j: "))
s = float(input("Задати значення пареметру s: "))
k = float(input("Задати значення пареметру k: "))

while j <= 0 and s < 2:
    print("Зауваження! \n   Має виконуватись умова: b ≥ 0")
    s = float(input("Задайте повторно значення параменту s : "))
print("Вхідні дані: j = %s; s = %s; k = %s" % (j, s, k))

if k > 0:
    f = j + (s * sqrt(k))
    print("k > 2; f =", round(f, 2))

elif k == 0:
    f = 5 - (2 - sqrt(s))
    print("k ≤ 2; f =", round(f, 2))
