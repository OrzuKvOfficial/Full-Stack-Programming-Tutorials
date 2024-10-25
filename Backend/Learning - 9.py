import pygame
import os

# Pygame kutubxonasini boshlash
pygame.mixer.init()

# Musiqa fayllarini topish funksiyasi
def find_music_files(directory):
    music_files = []
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            music_files.append(file)
    return music_files

# Musiqalarni ijro etish funksiyasi
def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    print(f"Ijro etilmoqda: {music_file}")

# Musiqa fayllarini qidirish
directory = "."  # Joriy papkani ko'rsatish
music_files = find_music_files(directory)

if not music_files:
    print("Musiqa fayllari topilmadi.")
else:
    print("Musiqalar ro'yxati:")
    for i, file in enumerate(music_files):
        print(f"{i + 1}. {file}")

    # Musiqa tanlash va ijro etish
    choice = int(input("Ijro etish uchun musiqaning raqamini kiriting: ")) - 1
    if 0 <= choice < len(music_files):
        play_music(music_files[choice])
    else:
        print("Notog'ri tanlov.")
