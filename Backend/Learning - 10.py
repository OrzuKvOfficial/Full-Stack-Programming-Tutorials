import time

# Soatning ishlash vaqtini va intervalini belgilash
working_time = 60  # Ishlash vaqti, masalan, 60 soniya
interval = 1  # Sekund oralig'ida vaqtni yangilash

# Soatni ishga tushirish
start_time = time.time()
current_time = 0

while current_time < working_time:
    # Hozirgi vaqtni hisoblash
    current_time = time.time() - start_time
    # Soat ko'rinishini yaratish
    minutes = int(current_time // 60)
    seconds = int(current_time % 60)
    print(f"{minutes:02}:{seconds:02}", end="\r")
    
    # Belgilangan intervalda kutish
    time.sleep(interval)
    
print("\nSoat tugadi!")
