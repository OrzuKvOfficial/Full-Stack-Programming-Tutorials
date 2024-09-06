# Oddiy hisoblash mashinasi
def calculator():
    print("Amallar: +, -, *, /")
    operation = input("Amalni tanlang: ")

    if operation in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Birinchi sonni kiriting: "))
            num2 = float(input("Ikkinchi sonni kiriting: "))

            if operation == '+':
                print(f"Natija: {num1} + {num2} = {num1 + num2}")
            elif operation == '-':
                print(f"Natija: {num1} - {num2} = {num1 - num2}")
            elif operation == '*':
                print(f"Natija: {num1} * {num2} = {num1 * num2}")
            elif operation == '/':
                if num2 != 0:
                    print(f"Natija: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Xatolik: nolga bo'lish mumkin emas!")
        except ValueError:
            print("Xatolik: raqamlarni to'g'ri kiriting!")
    else:
        print("Xatolik: noto'g'ri amal tanlandi!")

calculator()
