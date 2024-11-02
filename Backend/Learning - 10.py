from datetime import datetime

# Hozirgi vaqt va sanani olish
hozirgi_vaqt = datetime.now()

# Sanani formatlash
sana = hozirgi_vaqt.strftime("%Y-%m-%d")  # yil-oy-kun formatida
vaqt = hozirgi_vaqt.strftime("%H:%M:%S")  # soat:dakika:sekund formatida

# Natijani chop etish
print("Bugungi sana:", sana)
print("Hozirgi vaqt:", vaqt)
