dannye_prodazh = [
    {"name": "Ноутбук", "price": 50000, "quantity": 2},
    {"name": "Мышь", "price": 1000, "quantity": 10},
    {"name": "Ноутбук", "price": 50000, "quantity": 1},
    {"name": "Клавиатура", "price": 2000, "quantity": 5}
]

slovar_vyruchki = {} 

for zapis in dannye_prodazh:
    nazvanie = zapis["name"]
    vyruchka = zapis["price"] * zapis["quantity"]
    
    if nazvanie in slovar_vyruchki:
        slovar_vyruchki[nazvanie] += vyruchka
    else:
        slovar_vyruchki[nazvanie] = vyruchka

luchshiy_tovar = ""    
maks_vyruchka = 0     

for nazvanie, vyruchka in slovar_vyruchki.items():
    if vyruchka > maks_vyruchka:
        maks_vyruchka = vyruchka  
        luchshiy_tovar = nazvanie 


print("Выручка по каждому товару:", slovar_vyruchki)
print("Самый прибыльный товар:", luchshiy_tovar)
print("Количество уникальных наименований:", len(slovar_vyruchki))