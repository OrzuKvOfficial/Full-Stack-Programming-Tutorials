import RPi.GPIO as GPIO
import time

# GPIO pinlarni sozlash
PIR_PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)

print("Harakat sensori tayyor...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Harakat aniqlandi!")
            time.sleep(1)  # Harakat aniqlandi deb keyingi o'qishni kechiktiradi
        else:
            print("Harakat yo'q.")
        time.sleep(0.1)  # Sensorni qayta tekshirishdan oldin qisqa pauza
except KeyboardInterrupt:
    print("Programma to'xtatildi")
finally:
    GPIO.cleanup()
