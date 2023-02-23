from cmath import pi
from math import sqrt
from math import cos 
from math import sin 

text = "Колосов Ігор \n Індивідуальне Завдання 8" 
p = int(input("Введіть p: "))
q = int(input("Введіть q: "))
s = int(input("Введіть s: "))
t = int(input("Введіть t: "))

Result_1 = (sqrt(p*s)/(2*sqrt(7) - sqrt(5))**(q+t)) + (sqrt(q*t)/(2**q + 2**t))
Result_2 = (sqrt(abs(sin((4*pi)/sqrt(5)-p)-(s*t/sqrt(3))))**(sin(t-2*pi)))/(cos((2*pi)/s-q**2)**2-cos(pi/(q*t)-s)**2)
Result_3 =  sqrt((p+cos(3*pi+sqrt(5))**2)/(q**2+t**2)) + sin(pi/4-p**2)**3
Result_4 = abs(cos(2*pi+q)-t**s)/sqrt(q**(2*p))+p**t*cos(pi/4-p**2)
Result_5 = sqrt(7)/cos(3*pi*t)-sin(3*pi /p*q)**2-sqrt(2*q/s-3*t)**(2*pi)

print('Result_1 =', Result_1) 
print("Result_2 =", Result_2) 
print("Result_3 =", Result_3,) 
print("Result_4 =", Result_4,) 
print("Result_5 =", Result_5) 
