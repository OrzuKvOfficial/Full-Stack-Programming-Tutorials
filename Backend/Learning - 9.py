from googletrans import Translator

# Initialize the translator
translator = Translator()

# Original text in Uzbek
text = "yashash faqat Ruscha Englishcha"

# Translate to English
translated_text = translator.translate(text, src='uz', dest='en')

# Print the translation
print(translated_text.text)
