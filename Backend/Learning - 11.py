import os

def load_files(directory):
    files_data = {}
    
    # Papkada mavjud barcha fayllarni ko'rish
    for filename in os.listdir(directory):
        # Faqatgina asosiy fayllarni yuklash (masalan: `.txt` va `.csv`)
        if filename.endswith('.txt') or filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            
            # Faylni o'qish
            with open(file_path, 'r', encoding='utf-8') as file:
                files_data[filename] = file.read()
    
    return files_data

# Foydalanish
directory_path = 'your_directory_path_here'  # Fayllar saqlangan papka yo'lini kiriting
loaded_files = load_files(directory_path)

# Yuklangan fayllarni ko'rsatish
for filename, content in loaded_files.items():
    print(f"Fayl nomi: {filename}")
    print(f"Kontent:\n{content}\n")
