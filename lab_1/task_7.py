tarmin = 60 #минут
tarsms = 30 #sms
tarmb = 1024 #МБ
tartsena = 24.99 #руб. в месяц
dop1min = 0.89 #руб
dop1sms = 0.59 #руб
dop1mb = 0.79 #руб
nalog = 0.02 

izmin = input("Введите израсходованные за месяц минуты разговора (тариф включает в себя 60 минут): ")
iizmin = int(izmin)
izsms = input("Введите кол-во написаных sms за месяц (тариф включает в себя 30 смс): ")
iizsms = int(izsms)
izmb = input("Введите кол-во израсходованного интернет трафика в мб (тариф включает в себя 1024мб): ")
iizmb = int(izmb)

permin = tarmin - iizmin
persms = tarsms - iizsms
permb = tarmb - iizmb

tsenapermin = 0
tsenapersms = 0
tsenapermb = 0

if permin < 0 :
    permin = abs(permin)
    tsenapermin = permin * dop1min
    print("Сумма за одну дополнительную минуту составляет: ", dop1min ,"р.","\nВаша доплата за перерасход минут разговора составляет: ", f"{tsenapermin:.2f}", "р.")


if   persms < 0 :
    persms = abs(persms)
    tsenapersms = persms * dop1sms
    print("Сумма за одно дополнительное смс состовляет: ", dop1sms,"р.", "\nВаша доплата за перерасход смс составляет:", f"{tsenapersms:.2f}", "р.")

if   permb < 0 :
    permb = abs(permb)
    tsenapermb = persms * dop1mb
    print("Сумма за один дополнительный Мб составляет: ", dop1mb,"р.", "\nДоплата за перерасход итернет трафика составляет: ", f"{tsenapermb:.2f}", "р.")

ItogBN = tartsena + tsenapermin + tsenapersms + tsenapermb

Itog = ItogBN + ItogBN * nalog

print("Итоговая сумма к оплате (с учётом налога) составляет: ", f"{Itog:.2f}", "р.")


