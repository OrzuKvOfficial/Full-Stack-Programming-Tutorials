import os

# Zararli dasturlarni ko'rsatuvchi o'xshash so'zlar ro'yxati
malicious_patterns = ["malware", "trojan", "virus", "worm", "spyware", "adware"]

def scan_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read().lower()
            for pattern in malicious_patterns:
                if pattern in content:
                    print(f"[!] Zararli dastur alomati topildi: {pattern} faylda {file_path}")
                    return True
        return False
    except Exception as e:
        print(f"[X] Faylni o'qishda xato: {file_path} - {e}")
        return False

def scan_directory(directory):
    print(f"[INFO] Katalog skan qilinmoqda: {directory}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

# Misol uchun kompyuteringizdagi "C:\Users\username\Documents" katalogini skan qilish
scan_directory("C:/Users/username/Documents")
