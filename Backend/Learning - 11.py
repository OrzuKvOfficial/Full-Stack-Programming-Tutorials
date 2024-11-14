# Keldi yoki kelmadi dasturi
def ishga_kelganmi(odamlar):
    kelganlar = {}
    for odam in odamlar:
        javob = input(f"{odam} ishga keldimi? (ha/yo'q): ").strip().lower()
        if javob == "ha":
            kelganlar[odam] = "Keldi"
        else:
            kelganlar[odam] = "Kelmadi"
    return kelganlar

# Ishchilar ro'yxati
odamlar = ["Ali", "Vali", "Olim", "Oygul", "Aziza"]

# Natijalarni ko'rsatish
natija = ishga_kelganmi(odamlar)
print("\nIshga kelganlar ro'yxati:")
for odam, status in natija.items():
    print(f"{odam}: {status}")
