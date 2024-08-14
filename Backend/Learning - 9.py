from googletrans import Translator

# Tarjimon ob'ektini yaratamiz
translator = Translator()

# Tarjima qilmoqchi bo'lgan matningiz
text = "Hello, how are you?"

# Ingliz tilidan ispan tiliga tarjima qilish
translated = translator.translate(text, src='en', dest='es')

# Tarjimalangan matnni chop etish
print(translated.text)
