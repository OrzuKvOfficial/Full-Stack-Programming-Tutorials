from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate text from English to Russian
def translate_to_russian(text):
    translation = translator.translate(text, src='en', dest='ru')
    return translation.text

# Example usage
text_to_translate = "Hello, how are you?"
translated_text = translate_to_russian(text_to_translate)
print(f"Original: {text_to_translate}")
print(f"Translated: {translated_text}")
