cars = ["Toyota Camry", "Honda Accord", "Ford Mustang", "Chevrolet Corvette", "BMW 3 Series", "Mercedes-Benz C-Class", "Audi A4", "Tesla Model S"]
numbers = [3, 7, 1, 9, 4, 12, 8, 2, 15, 6]

#orted(cars, reverse=True) Bu listga tegmay hammasini  
#sorted(numbers, reverse=True) Bu list ichidagilariga tegmay ketma ket taxlaydi

#cars.reverse() Bu list ichidi hamma narsani ketma ket qila oladi

sonlar = len(cars)

qosh = list(range(0,12)) #Bu range so'zi sonlar qoshib beradi.

print(numbers)
print(cars)

toq = list(range(1,50,2)) #Bu yerda qadamini belgilash mumkun 2 yozse u 1 ta tashlab toq son qiladi
juft = list(range(0,20,2)) #Bu yerda qadamini belgilash mumkun 2 yozse u 1 ta tashlab juft son qiladi


katta = max(toq)
kichik = min(juft)

sum(numbers) #Bu list ichidagi qiymatlarni bir biriga qoshadi.


#Misol uchun 
 
treder = [20, 10,200, 20, 20, 20, 20, 20,20]
arzon = min(treder)
qimat = max(treder)
jami = sum(treder)

print('Kichik qiymat', arzon, 'Katta qiymat', qimat, 'Hammasi bolib', jami)

#List ichidan ajratib olish

print(cars[0:3]) #List ichidan kesib olish


#Listni nusxalash uchun

moshinlar = cars

cars.remove("Ford Mustang") #LIst ichidan keraaksiz malumotni kesib olish
print(cars)

print(sum)


# Listdagi elementlarni o'sish tartibida joylashtirish
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("O'sish tartibida:", sorted_numbers)

# Listdagi elementlarni kamayish tartibida joylashtirish
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Kamayish tartibida:", sorted_numbers_desc)
