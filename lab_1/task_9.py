tipizmer = input("Введите тип изверения (расстояние/вес): ")

if tipizmer == "расстояние":
    ishoded = input("Введите исходную единицу измерения (мм/см/дм/м/км): ")
    tselevaiaed = input("Введите целевую единицу измерения (мм/см/дм/м/км): ")

    z = input("Введите значение: ") #значение
    z = float(z)

    rasst = {'мм': 0.001, 'см':0.01, 'дм': 0.1,'м': 1, 'км': 1000}
    
    kish = rasst.get(ishoded)
    a = float(kish)
    ktsel = rasst.get(tselevaiaed)
    b = float(ktsel) 

    otvet = z * a / b
    print(f"{otvet:.7f}",tselevaiaed)

else:
    ishoded = input("Введите исходную единицу измерения (мг/г/кг/ц/т): ")
    tselevaiaed = input("Введите целевую единицу измерения (мг/г/кг/ц/т): ")

    z = input("Введите значение: ") #значение
    z = float(z)
    
    ves = {'мг': 0.000001, 'г':0.001, 'кг': 1,'ц': 100, 'т': 1000}
    kish = ves.get(ishoded)
    a = float(kish)
    ktsel = ves.get(tselevaiaed)
    b = float(ktsel) 

    otvet = z * a / b
    print(otvet,tselevaiaed)
    