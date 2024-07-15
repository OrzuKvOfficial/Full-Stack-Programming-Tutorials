#Created on Sun Jul 14 01:50:25 2024


a = 20
b = 5.5

tenp = 36.6

print(type(a))  #Bu Son yoki harifligini ajratish uchun 

son = 7_594_376_567 #Buni _ ajratish uchun qo'ysa tasiri yo'q

print("Aholi soni ", son)

x, y, z = 10, 8.8, -5

c = x*y
print(c)

b = 100/2 #float ko'rinishda
d = 100//2 #int ko'rinishda
print("float", b,"int", d )

radius = 50
PI = 3.15  #Dasurrchilar kelishgan holda Const qilingan lekin aslida bu O'zgaruvchi
diametr = 2*radius
print("Aylananing uzunligi = ", PI*diametr)


name = "Orzubek"
yo = 18
#yosh = str(yo)   #Bu katta xatolarr olib kelishi mumkun shu sabab qilishni mslaxat berilmaydi
xabar = name + ' ' + str(yo) + ' Yoshda' #Bu varyant to'g;ri
print(xabar)

l = int(input("Tug'ulgan yilni kiriting: "))
yosh = 2024 - l
print("Siz", yosh, "Yosh ekansiz")


#prompt = "Enter your birth year: "
#l = int(input(prompt))
#yosh = 2024 - l
#print("You are", yosh, "years old")


ab = int("10")
ba = float("10")
tena = str(36.6)
