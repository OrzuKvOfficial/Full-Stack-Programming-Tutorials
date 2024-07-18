bosh = []

ham = ["yog'", "piyoz", "kartoshka", "guruch"]

bosh.append(ham.pop(1))
print("Men olgan mahsulotlar:", bosh)
print("Qolgan mahsulotlar:", ham)

isim = ['Orzu', 'Airjon', 'Otabek']

name = ['Uzro', 'Xuy yuvoy']
print(name)
son = ['bir', 'ikki', 200, 300, 500, 800, 100,205]

cars = ['Bmw', "Audi", "Mers", "Ram"]
cars.sort() #Alfabed bilan taxlab beradi
print(cars)


isim.sort(reverse=True) #Alfabet bo'yicha faqqat teskari ketma ketlida taxlaydi
print(isim)

#orted(cars) #Bu faqat Consol uchun ketma ketlida taxlab beradi hech qanday Listni ichiga teymaydi
print(cars)

sorted(cars, reverse=True)
print(cars)

