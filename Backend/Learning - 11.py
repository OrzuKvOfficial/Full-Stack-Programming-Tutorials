import requests

# Yuklab olmoqchi bo'lgan fayl URL manzili
file_url = "https://example.com/sample.docx"

# Faylni yuklab olish va saqlash funksiyasi
def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Xatoliklarni tekshiradi
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # Bo'sh bo'lmagan ma'lumotlarni yozadi
                    file.write(chunk)
        print(f"Fayl muvaffaqiyatli saqlandi: {save_path}")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

# Saqlanadigan fayl nomi
save_path = "sample.docx"

# Funktsiyani chaqirish
download_file(file_url, save_path)
