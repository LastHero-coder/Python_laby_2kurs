bd = input("Введите вашу дату рождения: \n(Пример: 12.03.2008): ") #birthday

d = bd[0]+bd[1] #day
d = int(d)
m = bd[3]+ bd[4] #month

tr=True

if d >= 21 and d<=31 and m == "03" or d <= 19 and d >=1 and m == "04":
    tr = False
    print("Ваш знак зодиака - овен")

if d >= 20 and d<=30 and m == "04" or d <= 20 and d >=1 and m == "05":
    tr = False
    print("Ваш знак зодиака - телец")

if d >= 21 and d<=31 and m == "05" or d <= 20 and d >=1 and m == "06":
    tr = False
    print("Ваш знак зодиака - близнецы")

if d >= 21 and d<=30 and m == "06" or d <= 22 and d >=1 and m == "07":
    tr = False
    print("Ваш знак зодиака - рак")

if d >= 23 and d<=31 and m == "07" or d <= 22 and d >=1 and m == "08":
    tr = False
    print("Ваш знак зодиака - лев")

if d >= 23 and d<=31 and m == "08" or d <= 22 and d >=1 and m == "09":
    tr = False
    print("Ваш знак зодиака - дева")

if d >= 23 and d<=30 and m == "09" or d <= 22 and d >=1 and m == "10":
    tr = False
    print("Ваш знак зодиака - весы")

if d >= 23 and d<=31 and m == "10" or d <= 21 and d >=1 and m == "11":
    tr = False
    print("Ваш знак зодиака - скорпион")

if d >= 22 and d<=30 and m == "11" or d <= 21 and d >=1 and m == "12":
    tr = False
    print("Ваш знак зодиака - стрелец")

if d >= 22 and d<=31 and m == "12" or d <= 19 and d >=1 and m == "01":
    tr = False
    print("Ваш знак зодиака - козерог")

if d >= 20 and d<=31 and m == "01" or d <= 18 and d >=1 and m == "02":
    tr = False
    print("Ваш знак зодиака - водолей")

if d >= 19 and d<=28 and m == "02"  or d <= 20 and d >=1 and m == "03":
    tr = False
    print("Ваш знак зодиака - рыбы")

if d == 29 and m == "02":
    tr = False
    print("Ваш знак зодиака - рыбы")

if tr:
    print("Вы некорректно ввели дату")
