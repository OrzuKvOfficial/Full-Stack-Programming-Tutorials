# Listni yig'uvchi programma
def list_yiguvchi():
    asosiy_list = []  # Bo'sh list yaratamiz
    print("Listni to'ldirishni boshlang. Tugatish uchun 'exit' kiriting.")
    
    while True:
        element = input("Element kiriting: ")
        
        if element.lower() == 'exit':  # Agar foydalanuvchi 'exit' yozsa, dastur to'xtaydi
            break
        
        asosiy_list.append(element)  # Kiritilgan elementni listga qo'shamiz
    
    print("\nYakuniy ro'yxat:")
    print(asosiy_list)

# Funktsiyani chaqiramiz
list_yiguvchi()
