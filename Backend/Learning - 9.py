import random

def math_game():
    print("Matematika o'yiniga xush kelibsiz!")
    
    # 10 ta savol beramiz
    correct_answers = 0
    for i in range(10):
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*'])
        
        if operation == '+':
            correct_result = number1 + number2
        elif operation == '-':
            correct_result = number1 - number2
        else:
            correct_result = number1 * number2
        
        # Savolni chiqaramiz
        print(f"Savol {i+1}: {number1} {operation} {number2} = ?")
        user_answer = int(input("Javobingiz: "))
        
        # Javobni tekshiramiz
        if user_answer == correct_result:
            print("To'g'ri!")
            correct_answers += 1
        else:
            print(f"Noto'g'ri. To'g'ri javob: {correct_result}")
    
    # Natija
    print(f"O'yin tugadi! Siz {correct_answers} ta to'g'ri javob berdingiz.")

# Dastur ishga tushadi
math_game()
