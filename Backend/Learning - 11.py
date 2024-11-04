from datetime import datetime

# To-do ro'yxati uchun bo'sh list
todo_list = []

def show_time():
    """Joriy vaqtni ko'rsatadi."""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Joriy vaqt:", current_time)

def add_todo(task):
    """Yangi vazifani ro'yxatga qo'shadi."""
    todo_list.append(task)
    print(f"Vazifa qo'shildi: {task}")

def show_todo():
    """To-do ro'yxatini ko'rsatadi."""
    if todo_list:
        print("To-do ro'yxati:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("To-do ro'yxati bo'sh.")

def calculate(expression):
    """Matematik ifodani hisoblaydi."""
    try:
        result = eval(expression)
        print(f"Natija: {result}")
    except Exception as e:
        print("Xato:", e)

def main():
    print("Botga xush kelibsiz!")
    while True:
        print("\nQuyidagi buyruqlardan birini kiriting: 'vaqt', 'todo qo'shish', 'todo ko'rsatish', 'hisob', 'chiqish'")
        command = input("Buyruq kiriting: ").lower()

        if command == 'vaqt':
            show_time()
        elif command == 'todo qo\'shish':
            task = input("Vazifa kiriting: ")
            add_todo(task)
        elif command == 'todo ko\'rsatish':
            show_todo()
        elif command == 'hisob':
            expression = input("Ifodani kiriting (masalan, 2+2): ")
            calculate(expression)
        elif command == 'chiqish':
            print("Botdan chiqildi.")
            break
        else:
            print("Noto'g'ri buyruq, qayta urinib ko'ring.")

if __name__ == "__main__":
    main()
