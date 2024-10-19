import requests

# Valyuta kurslarini olish uchun API'ni qo'llash
def get_exchange_rate():
    # OpenExchangeRates yoki boshqa xizmatdan API kalitni qo'shishingiz kerak bo'ladi
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    # API'dan valyuta kurslarini olish
    response = requests.get(api_url)
    data = response.json()
    
    # So'm kursini olish
    return data["rates"]["UZS"]

# Foydalanuvchi qancha dollar borligini kiritadi
dollar_amount = float(input("Dollarda qancha mablag' bor? "))

# Dollar-to-sum kursini olish
dollar_to_sum = get_exchange_rate()

# So'mdagi mablag'ni hisoblash
sum_amount = dollar_amount * dollar_to_sum

print(f"{dollar_amount} AQSh dollari {sum_amount:.2f} so'mga teng.")
