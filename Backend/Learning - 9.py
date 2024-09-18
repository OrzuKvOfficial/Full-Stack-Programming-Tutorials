from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Function to translate text to any language
def translate_text(text, src_lang='en', dest_lang='ru'):
    try:
        # Perform translation
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to display available languages
def display_languages():
    print("Supported languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")

# Main bot logic
def translation_bot():
    print("Welcome to the Translation Bot!")
    display_languages()

    src_lang = input("Enter source language code (default is 'en' for English): ") or 'en'
    dest_lang = input("Enter target language code (default is 'ru' for Russian): ") or 'ru'
    
    text_to_translate = input("Enter the text you want to translate: ")

    translated_text = translate_text(text_to_translate, src_lang, dest_lang)
    
    print(f"\nOriginal text: {text_to_translate}")
    print(f"Translated text: {translated_text}")

# Run the bot
if __name__ == "__main__":
    translation_bot()
