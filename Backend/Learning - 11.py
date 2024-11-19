# Foydalanuvchidan bir nechta ma'lumotni olish
data = input("Ismingiz va yoshingizni kiriting (Masalan: Orzubek, 18): ")

# Ma'lumotlarni ajratish
name, age = data.split(", ")
age = int(age)

# Formatlangan chiqish
print(f"Salom, {name}! Siz {age} yoshdasiz.")
