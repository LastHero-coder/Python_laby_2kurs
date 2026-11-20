word = input("Введите строку: ")

tr = True

wort=word.split()
word= "".join(wort)
word =str(word)

lens = len(word)
i = 0

while i != lens//2 :
    if word[i]==word[lens-1-i]:
        i+=1
        continue
    else:
        print("Ваша строка не является палиндромом")
        tr = False
        break

if tr:
    print("Ваша строка является палиндромом!")

#Привер: нажал кабан на баклажан; там холм лохмат
#        топот, шалаш