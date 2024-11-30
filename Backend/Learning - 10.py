import re  # Matnlarni tahlil qilish uchun
import operator

# Hisoblash funksiyasi
def calculate(expression):
    try:
        # Amal va operandlarni aniqlash
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        
        # Matndan amal va sonlarni ajratib olish
        tokens = re.findall(r'\d+|\+|\-|\*|\/', expression)
        if len(tokens) < 3:
            return "Noto'g'ri format! Masalan, '5 + 6' kiriting."
        
        # Son va amallarni hisoblash
        num1, op, num2 = int(tokens[0]), tokens[1], int(tokens[2])
        if op in ops:
            result = ops[op](num1, num2)
            return f"Natija: {result}"
        else:
            return "Amal noto'g'ri! Faqat +, -, *, / ishlatiladi."
    except Exception as e:
        return f"Xato yuz berdi: {e}"

# Asosiy dastur
print("Oddiy sun'iy intellekt kalkulyatoriga xush kelibsiz!")
print("Masalan: '5 + 6' yoki '10 / 2' kabi matematik ifodalarni kiriting.")
while True:
    user_input = input("Iltimos, hisoblashni kiriting (yoki 'chiqish' deb yozing): ").lower()
    if user_input == "chiqish":
        print("Dasturdan chiqildi!")
        break
    print(calculate(user_input))
