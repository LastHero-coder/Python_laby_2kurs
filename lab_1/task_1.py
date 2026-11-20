prov = True
while prov :
    print(f"Введите ваше ФИО:")
    fio = input()
    FIO = fio.split()#разбивает чтроку по пробелам

    if FIO[0] == 0 or FIO[1] == 0 or FIO[2] ==0:
        print ("Вы не ввели ФИО полностью, сделайте ещё одну попытку: ")
    else:
        break

Imia = FIO[1]
Otch = FIO[2]

I = Imia[0]
FIO.insert(1, I)

O = Otch[0]
FIO.insert(2, O)

print(f"Здравствуйте, {FIO[0]} {FIO[1]}.{FIO[2]}.!")