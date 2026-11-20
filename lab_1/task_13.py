vvodpolzovatelya = input("Введите числа через пробел (целые или дробные): ")

strokinachisel = vvodpolzovatelya.split()
spisokchisel = [] 

for element in strokinachisel:
    if '.' in element:
        spisokchisel.append(float(element))
    else:
        spisokchisel.append(int(element))

print(f"Вы ввели массив чисел: {spisokchisel}\n")

if len(spisokchisel) == 0:
    print("Вы не ввели ни одного числа.")
else:

    
    unikalnyechisla = []
    for chislo in spisokchisel:
        if chislo not in unikalnyechisla:
            unikalnyechisla.append(chislo)
    print("1. Уникальные числа:", unikalnyechisla)

    
    povtoryayushchiesyachisla = []
    for chislo in spisokchisel:
        if spisokchisel.count(chislo) > 1 and chislo not in povtoryayushchiesyachisla:
            povtoryayushchiesyachisla.append(chislo)
    print("2. Повторяющиеся числа:", povtoryayushchiesyachisla)

    
    chetnyechisla = []
    nechetnyechisla = []
    for chislo in spisokchisel:
        if type(chislo) == int: 
            if chislo % 2 == 0:
                chetnyechisla.append(chislo)
            else:
                nechetnyechisla.append(chislo)
    print("3. Четные числа:", chetnyechisla)
    print("   Нечетные числа:", nechetnyechisla)

    
    otritsatelnyechisla = []
    for chislo in spisokchisel:
        if chislo < 0:
            otritsatelnyechisla.append(chislo)
    print("4. Отрицательные числа:", otritsatelnyechisla)

    
    drobnyechisla = []
    for chislo in spisokchisel:
        if type(chislo) == float: 
            drobnyechisla.append(chislo)
    print("5. Числа с плавающей точкой:", drobnyechisla)

    
    summakratnyh5 = 0
    for chislo in spisokchisel:
        if chislo % 5 == 0:
            summakratnyh5 = summakratnyh5 + chislo
    print("6. Сумма чисел, кратных 5:", summakratnyh5)

    
    maksimalnoechislo = spisokchisel[0] 
    for chislo in spisokchisel:
        if chislo > maksimalnoechislo:
            maksimalnoechislo = chislo
    print("7. Самое большое число:", maksimalnoechislo)

    
    minimalnoechislo = spisokchisel[0] 
    for chislo in spisokchisel:
        if chislo < minimalnoechislo:
            minimalnoechislo = chislo
    print("8. Самое маленькое число:", minimalnoechislo)