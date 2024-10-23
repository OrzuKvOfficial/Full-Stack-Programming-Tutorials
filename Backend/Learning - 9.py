# Tezlikni hisoblash uchun programma
# Formula: tezlik = masofa / vaqt

# Masofa (kilometr) va vaqt (soat) kiriting
masofa = float(input("Masofani kiriting (km): "))
vaqt = float(input("Vaqtni kiriting (soat): "))

# Tezlikni hisoblash
if vaqt > 0:
    tezlik = masofa / vaqt
    print(f"Tezlik: {tezlik} km/soat")
else:
    print("Vaqt 0 dan katta bo'lishi kerak.")

