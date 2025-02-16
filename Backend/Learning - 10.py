from googletrans import Translator

def translate_text(text, dest_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Foydalanish
text = "Salom, qalaysiz?"
translated_text = translate_text(text, 'es')  # Ispan tiliga tarjima qilish
print(translated_text)
