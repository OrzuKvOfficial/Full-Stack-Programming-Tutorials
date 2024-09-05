import RPi.GPIO as GPIO
import time

# GPIO ayarları
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7  # PIR sensörünü bağladığınız pin numarası

# PIR sensörü için ayar
GPIO.setup(PIR_PIN, GPIO.IN)

# Hareket algılandığında tetiklenecek fonksiyon
def hareket_algilandi(channel):
    print("Hareket algılandı!")

# PIR pinine olay ekleme
GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=hareket_algilandi)

try:
    print("Hareket algılanıyor...")
    while True:
        time.sleep(1)  # Sürekli olarak çalışır ve hareketi kontrol eder
except KeyboardInterrupt:
    print("Program sonlandırıldı")
finally:
    GPIO.cleanup()  # GPIO ayarlarını sıfırlar
