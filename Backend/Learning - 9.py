# Vazn va bo'y bo'yicha kunlik suv miqdorini hisoblash
def daily_water_intake(weight_kg):
    # Har bir kilogramm vazn uchun 30-35 ml suv ichish tavsiya qilinadi
    # O'rtacha hisobda har kg uchun 32.5 ml suv ichish kerak
    water_ml_per_kg = 32.5
    daily_intake_ml = weight_kg * water_ml_per_kg  # kunlik suv miqdori (ml)
    daily_intake_l = daily_intake_ml / 1000  # litrga o'tkazamiz
    return daily_intake_l

# Oylik suv miqdorini hisoblash
def monthly_water_intake(weight_kg):
    daily_intake_l = daily_water_intake(weight_kg)
    monthly_intake_l = daily_intake_l * 30  # 1 oyda 30 kun bor deb hisoblaymiz
    return monthly_intake_l

# Foydalanuvchi ma'lumotlarini kiritadi
weight_kg = float(input("Vazningizni kilogrammda kiriting: "))
height_cm = float(input("Bo'yingizni santimetrda kiriting: "))

# Natijalarni hisoblash va chiqarish
daily_water = daily_water_intake(weight_kg)
monthly_water = monthly_water_intake(weight_kg)

print(f"Sizning bir kunda ichishingiz kerak bo'lgan suv miqdori: {daily_water:.2f} litr.")
print(f"Sizning bir oyda ichishingiz kerak bo'lgan suv miqdori: {monthly_water:.2f} litr.")
