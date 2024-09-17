import os
import time

# Fayl katalogini ko'rsatamiz
directory = "/sizning/katalogingiz"

# Dastur boshlanishida barcha fayllarni o'qish
initial_files = {f: os.path.getmtime(os.path.join(directory, f)) for f in os.listdir(directory)}

while True:
    current_files = {f: os.path.getmtime(os.path.join(directory, f)) for f in os.listdir(directory)}

    # Yangi fayllarni topish
    new_files = [f for f in current_files if f not in initial_files]
    if new_files:
        print(f"Yangi fayllar: {new_files}")

    # O'zgargan fayllarni topish
    modified_files = [f for f in current_files if f in initial_files and current_files[f] != initial_files[f]]
    if modified_files:
        print(f"O'zgartirilgan fayllar: {modified_files}")

    # Fayllar ro'yxatini yangilaymiz
    initial_files = current_files

    # Har bir 10 soniyada tekshirib turish
    time.sleep(10)
