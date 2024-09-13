import os

# Musiqa fayllari uchun ruxsat etilgan formatlar
ALLOWED_EXTENSIONS = ['mp3', 'wav', 'flac', 'aac']

# Faylning kengaytmasini tekshirish
def is_music_file(filename):
    return filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS

# Berilgan katalogdagi barcha musiqa fayllarini saralash
def list_music_files(directory):
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if is_music_file(file):
                music_files.append(os.path.join(root, file))
    return music_files

# Musiqa fayllari orasida qidiruv
def search_music_files(directory, search_query):
    music_files = list_music_files(directory)
    found_files = [file for file in music_files if search_query.lower() in os.path.basename(file).lower()]
    return found_files

# Katalogni kiritish va qidiruvni amalga oshirish
directory = input("Musiqa fayllari saqlangan katalogni kiriting: ")
search_query = input("Qidirilayotgan musiqa nomi yoki qismidan parcha kiriting: ")

found_files = search_music_files(directory, search_query)

if found_files:
    print(f"Topilgan fayllar ({len(found_files)} ta):")
    for file in found_files:
        print(file)
else:
    print("Hech qanday fayl topilmadi.")
