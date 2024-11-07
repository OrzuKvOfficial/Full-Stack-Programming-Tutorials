import re

def find_phone_numbers(text):
    phone_pattern = r"\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}"

    phone_numbers = re.findall(phone_pattern, text)
    
    return phone_numbers

text = """
