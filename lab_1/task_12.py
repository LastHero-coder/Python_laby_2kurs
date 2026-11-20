text = input("Введите текст: ").lower()
slova = text.split()

dlina = len(slova)
print("Общее кол-во слов составляет: ", dlina)

chastotaslov = {}
for word in slova:
    if word in chastotaslov:
        chastotaslov[word] += 1
    else:
        chastotaslov[word] = 1

print("В тексте: ")
for word, count in chastotaslov.items():
    print(count, " " , word)

maxchastslovo = ""
maxcount = 0 
for chastslovo, countt in chastotaslov.items():
    if countt > maxcount:
        maxcount = countt
        maxchastslovo = chastslovo

print("Самое частое слово: ", maxchastslovo)

shortest_word = slova[0]
longest_word = slova[0]

for word in slova:
    if len(word) < len(shortest_word):
        shortest_word = word
    if len(word) > len(longest_word):
        longest_word = word

print("самое короткое слово:", shortest_word)
print("самое длинное слово:", longest_word)
#////////////////////////////////////////////////
#///////////////////////////////////////////////
print("\nПосле отброса слов короче чем 3 буквы:")

slova3 = []
for word in slova:  
    if len(word) >= 3:
        slova3.append(word)

dlina = len(slova3)
print("Общее кол-во слов составляет: ", dlina)

chastotaslov = {}
for word in slova3:
    if word in chastotaslov:
        chastotaslov[word] += 1
    else:
        chastotaslov[word] = 1

print("В тексте: ")
for word, count in chastotaslov.items():
    print(count, " " , word)

maxchastslovo = ""
maxcount = 0 
for chastslovo, countt in chastotaslov.items():
    if countt > maxcount:
        maxcount = countt
        maxchastslovo = chastslovo

print("Самое частое слово: ", maxchastslovo)

shortest_word = slova3[0]
longest_word = slova3[0]

for word in slova3:
    if len(word) < len(shortest_word):
        shortest_word = word
    if len(word) > len(longest_word):
        longest_word = word

print("самое короткое слово:", shortest_word)
print("самое длинное слово:", longest_word)