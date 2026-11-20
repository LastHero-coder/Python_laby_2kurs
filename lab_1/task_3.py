sum = input("Введите целую сумму: ")
summa = int(sum)

count100 = 0
count50 = 0
count10 = 0
count5 = 0
count2 = 0
count1 = 0

while summa >=100:
    #print ("можно использовать купюру 100р ")
    summa -= 100
    count100 +=1

while summa >=50 :
    #print ("можно использовать купюру 50р")
    summa -= 50
    count50 +=1

while summa >=10:
    #print ("можно использовать купуру 10р")
    summa -= 10       
    count10 += 1

while summa >=5:
    #print ("можно использовать купуру 5р")
    summa -= 5       
    count5 += 1

while summa >=2:
    #print ("можно использовать монету 2р")
    summa -= 2       
    count2 += 1

while summa >=1:
    #print ("можно использовать купуру 1р")
    summa -= 1       
    count1 += 1

print("введёную сумму можно разбить на: ")
if count100 > 0:
    print(count100, "по 100руб")
if count50 > 0:
    print(count50, "по 50руб")
if count10 > 0:
    print(count10, "по 10руб")
if count5 > 0:
    print(count5, "по 5руб")
if count2 > 0:
    print(count2, "по 2руб")
if count1 > 0:    
    print(count1, "по 1руб")