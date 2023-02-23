text = "CS-21-1"
p = -1
q = 2
u = 5
v = -3
spisok = [0.1, 2.61, -0.82, -4.3, 5.7, -9, -3.71, 8.52, 2.58, -1.15]
#ваш код в репорте зачастую выглядит примерно так:
result_1=((3*u)/(4*p))+((2*p+7*q)/(3*q))-((q)/(5*u))+((3*u)/(2*v))
result_2=((p-q)/(p*q)+(p*q)/(p-q))*(((u-v)/(u*v)) + (v/u))
result_3=((p**2)/(2*q))+(q**3/(4*p))-u**-3/(3*v)+(v**-2/u)
result_4=((2*p**2+5*v)/(q**2+u**2))-((3*v + u)/(p**2+q**2))+(u*p**2)/(5*v)
result_5=(u**2+u*v+v**2-p**2-p*q-q**2)/(p**2+q**2*u**2+v**2)
result_6=p**(2*u-3*q) + 2*q**(3*p+1)-4**(2*v+3)
result_7=((2*u**(3*v))/(3*p+4**(u-2)))+((p**2-3*q**3)**(u-v))/3**(u-1)-((u*v)/(p*q))**(u+v)
result_8=(q**(4*u-1)+3**(2*p)-2*u**v)/(5**(u-2*v-1))+(p**(3-q))/(3**(u+v))-(u**(q+2))/(2**q+3**(v-1))
result_9=(u*spisok[1])/(p*q*spisok[0])-(spisok[4]*spisok[8])/(u*v*spisok[5])
result_10=(spisok[0]**2/p**2)+(spisok[1]/q**-2)+(spisok[3]**3/u**p)-(spisok[5]/v**-q)
#потому то вас никто не уважает, никто не слушает, а ваши работы делаются в последнюю очередь,
#и я не имею ни малейшего желания переписывать тонны формул по кривым вашим репортам где черт ногу сломит, 
#уж темболее если мне не платят
print(text, "\n")

print("result_1", result_1)
print("result_2", result_2)
print("result_3", result_3)
print("result_4", result_4)
print("result_5", result_5)
print("result_6", result_6)
print("result_7", result_7)
print("result_8", result_8)
print("result_9", result_9)
print("result_10", result_10)

print("result_1 < result_2", result_1 < result_2)
print("result_3 < result_4", result_3 < result_4)
print("result_5 < result_6", result_5 < result_6)
print("result_7 < result_8", result_7 < result_8)
print("result_9 < result_10", result_9 < result_10)

Result_list = [
    round(result_1,3),
    round(result_2,3),
    round(result_3,3),
    round(result_4,3),
    round(result_5,3),
    round(result_6,3),
    round(result_7,3),
    round(result_8,3),
    round(result_9,3),
    round(result_10,3)
]

print("Result_list: ", Result_list)
Result_list.sort()
Result_list.reverse()
print("сортир")
max = max(Result_list)
min = min(Result_list)
print("\n Max = ",max,"Min = ",min)