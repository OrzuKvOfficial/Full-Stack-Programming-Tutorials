import re

def find_phone_numbers(text):
    # Telefon raqami formatiga mos keluvchi regex
    phone_pattern = r"\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}"
    
    # Muntazam ifoda bo‘yicha barcha mos keluvchi raqamlarni topamiz
    phone_numbers = re.findall(phone_pattern, text)
    
    return phone_numbers

# Sinov matni
text = """
Mana mening telefon raqamlarim: +1 347 841 4140 yoki (347) 841-4140.
Mening boshqa telefon raqamim +998-90-123-45-67.
"""

# Telefon raqamlarini topish
found_numbers = find_phone_numbers(text)
print("Topilgan telefon raqamlari:", found_numbers)
