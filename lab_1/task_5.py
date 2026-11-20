a = input("Введите a: ")
b = input("Введите b: ")
oper = input("Введите операцию: ")

a=float(a)
b=float(b)

if oper == '+':
    print("Ответ: ", a + b)

if oper == '-':
    print("Ответ: ", a - b)

if oper == '*':
    print("Ответ: ", a * b)

if oper == '/':
    if b==0:
        print("На ноль делить нельзя)")
    else:
        rez = a/b
        print("Ответ: ", rez)

if oper == '%':
    if b==0:
        print("На ноль делить нельзя! ")
    else:
        print("Ответ: ", a % b)

if oper == "**":
    print("Ответ: ", a ** b)




