# Faylni ochish va har bir qatorni alohida o'qish
with open('fayl_nomi.txt', 'r') as fayl:
    qatorlar = fayl.readlines()

# O'qilgan ma'lumotni chop etish
for qator in qatorlar:
    print(qator.strip())
