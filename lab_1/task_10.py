sumP = input("Введите сумму покупки (руб): ")
sumP = int(sumP)
age = input("Введите ваш возраст: ")
age = int(age)
dr = input("У вас сегодня деньрождение? (да/нет): ")
vip = input("Вы VIP клиент? (да/нет): ")

skidka = 0

if sumP > 1000 :
    skidka += 0.1

if age >= 63 :
    skidka += 0.05

if dr == "да" :
    skidka += 0.05

if vip == "да":
    skidka += 0.15

if skidka > 0.25:
    skidka = 0.25

print ("Итоговая сумма к оплате, с учётом скидок составит: ", sumP-sumP*skidka, "руб.")