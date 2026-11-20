Prov = True
while Prov:
    password = input ("Введите НАДЁЖНЫЙ пароль: \n Требования: \n      1. От 16 символов \n      2. Присутствие и цифр, и букв: ")
    
    if len(password) < 16:
        print("Пароль меньше 16 символов, попробуй ещё раз)")
        continue

    digit = False
    letter = False

    for char in password:
        if char.isdigit():
            digit=True
        if char.isalpha():
            letter=True

    if digit and letter:
        print("Отлично! Ваш пароль надёжный! ")
        break

    else:
        print("Ваш пароль не достаточно надёжный, попробуй ещё раз ")