import sounddevice as sd
from scipy.io.wavfile import write

# Parametrlar
sample_rate = 44100  # Ovoz namuna olish chastotasi (Hz)
duration = 10  # Yozib olish davomiyligi (soniya)

print("Ovoz yozib olinmoqda...")

# Ovoz yozib olish
recording = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=2)
sd.wait()  # Yozib olish tugaguncha kutish

# Faylga saqlash
write("output.wav", sample_rate, recording)

print("Ovoz muvaffaqiyatli yozib olindi va 'output.wav' fayliga saqlandi.")
