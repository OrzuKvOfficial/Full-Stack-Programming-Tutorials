import os

# Zararli dastur imzolarini aniqlash uchun oddiy ro'yxat
malicious_signatures = [
    "malware_signature_1",
    "virus_signature_2",
    "dangerous_code_3"
]

# Berilgan faylning zararli kodini tekshirish funksiyasi
def scan_file(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as file:
            file_content = file.read()
            for signature in malicious_signatures:
                if signature in file_content:
                    return True
        return False
    except:
        return False

# Fayllarni katalog bo'ylab skanerlash funksiyasi
def scan_directory(directory_path):
    infected_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if scan_file(file_path):
                infected_files.append(file_path)
    return infected_files

# Bosh katalogni skanerlash
directory_to_scan = input("Katalogni kiriting: ")
infected_files = scan_directory(directory_to_scan)

if infected_files:
    print("Zararli fayllar topildi:")
    for file in infected_files:
        print(file)
else:
    print("Hammasi toza, zararli fayllar topilmadi.")
