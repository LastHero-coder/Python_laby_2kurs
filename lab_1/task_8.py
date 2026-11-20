import random

zagchislo = random.choice(range(1,101))
pop = 0
pop = input("Привет, мешок с костями! Я загадал число от 1 до 100 включая, попробуй угадать ... ;)\nВведите число: ")
count = 1
pop = int(pop)

while pop != zagchislo:
 
    if pop == zagchislo:
        break

    count += 1

    if pop > zagchislo:
        pop = input("Число, которое я загадал, меньше твоего, попробуй ещё раз: ")
        pop = int(pop)
    else :
        pop = input("Число, которое я загадал, больше твоего, попробуй ещё раз: ")
        pop = int(pop)

print("В яблочко! Загаданное число было:", zagchislo,", ты потратил всего ", count, "попыток, молодец!")