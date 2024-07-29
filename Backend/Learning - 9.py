def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Bo'lish amali nolga bo'linmaydi"
    return x / y

def calculator():
    print("Kalkulyator dasturiga xush kelibsiz!")
    print("Quyidagi amallarni bajara olasiz:")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")

    while True:
        choice = input("Amalni tanlang (1/2/3/4) yoki dasturdan chiqish uchun 'q' tugmasini bosing: ")

        if choice == 'q':
            print("Dasturdan chiqmoqda...")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Birinchi sonni kiriting: "))
            num2 = float(input("Ikkinchi sonni kiriting: "))

            if choice == '1':
                print(f"Natija: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Natija: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Natija: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Natija: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")

calculator()
