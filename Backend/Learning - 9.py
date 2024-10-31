from langdetect import detect, DetectorFactory

# Natijani tasodifiylikka qarshi barqaror qilish
DetectorFactory.seed = 0

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Language could not be detected."

# Foydalanish
text = "Bu yerda siz matnni kiriting."
print(f"Tilingiz: {detect_language(text)}")
