#Created on Sun Jul 14 00:24:04 2024


name = 'Orzubek'
nLast = 'Kamariddinoov'

#f"Mening Ismim {name})" Terminalga kiritilganda Matin yoki son qoshish mumkun

fullname = f"{name} {nLast}"

print(fullname)

print(name + ' ' + nLast)



print(f"Hello my name is {name}. My last name is {nLast}")


print('Hello World')
print('Hello \tWorld')
print('Hello \nWorld')

#Upper
print(fullname.upper()) #upper yangi qoshimcha katta harf qilib beradi.
fullname = fullname.upper()  #Bu yerda upper O'zgaruvchini o'zgartiradi kattaga.

#Lower
print(fullname.lower()) #lower hamma hariflarni kichik shakilga o'zgartiradi.

#Titele 
print(fullname.title()) #Har bir so'zning bosh xarfini katta qiladi.

#capitalize
print((fullname.capitalize())) #Gapda birinchi xarifni katta qilib beradi

#Lstrip
frutes = "   apple   "
print(frutes)
print(frutes.lstrip() + "Yaxshi ko'raman") #Chap tomondagi bo'shliqni olib tashlaydi

#Rstrip
print(frutes.rstrip() + "Yaxshi ko'raman") #O'ng tarafdagi bo'shliqni olib tashlaydi

#Strip
print(frutes.strip() + "Yaxshi ko'raman") #Ikki yondagi bo'shliqni olib tashlaydi.
 

#Malumootni qabul qilish
manba = input("Ismingizni kiriting...") #Malumotlar kiritish mumkun
print("Assalomu Alaykum, " + manba)
manba = input("Ismingiz nima?\n>>>>>")
print("Assalomu alaykum, " + manba.title())