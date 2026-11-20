list = input("Введите первый набор чисел через пробел: ")
list = list.split()
list1 = []
for element in list:
    if '.' in element:
        list1.append(float(element))
    else:
        list1.append(int(element))

list = input("Введите второй набор чисел через пробел: ")
list = list.split()
list2 = []
for element in list:
    if '.' in element:
        list2.append(float(element))
    else:
        list2.append(int(element))

both = []
for element in list1:
    if element in list2 and element not in both:
        both.append(element)
print("В двух списках: ", both)

only1 = []
for element in list1:
    if element not in list2 and element not in only1:
        only1.append(element)

print("Элементы существующие только в первом наборе: ", only1)

only2 = []
for element in list2:
    if element not in list1 and element not in only1:
        only2.append(element)

print("Элементы существующие только во втором наборе: ", only2)

ostalnye = []
for element in only1:
    ostalnye.append(element)
for element in only2:
    ostalnye.append(element)

print ("Числа из обоих наборов, за исключением чисел, найденных в пункте 1: ", ostalnye )