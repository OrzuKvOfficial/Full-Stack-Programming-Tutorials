def tekshirish(kod):
    try:
        exec(kod)
        print("Kod muvaffaqiyatli bajarildi.")
    except Exception as e:
        print(f"Kodda xatolik: {e}")

kod = """
for i in range(5):
    print(i)
"""

tekshirish(kod)
