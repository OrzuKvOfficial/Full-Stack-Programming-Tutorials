import time

# Vazn yo'qotish bo'yicha maslahatlar
tips = [
    "Suvni ko'proq iching!",
    "Ko'proq harakat qiling, masalan, piyoda yuring!",
    "Sog'lom ovqatlaning, sabzavotlar va mevalarni ko'paytiring!",
    "Kundalik kaloriya hisobini olib boring!",
    "Kecha ovqatlanishni kamaytiring va uyquga e'tibor bering!"
]

# Eslatma funksiyasi
def weight_loss_reminder(interval, repetitions):
    for i in range(repetitions):
        tip = tips[i % len(tips)]  # Maslahatlarni aylantirib chiqarish
        print(f"Eslatma: {tip}")
        time.sleep(interval)  # Belgilangan vaqt oralig'ida kutish (sekundda)

# Har 10 soniyada 5 eslatma chiqarish
weight_loss_reminder(10, 5)
