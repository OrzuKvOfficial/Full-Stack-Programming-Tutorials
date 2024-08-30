import requests

# Ma'lumotlar olish uchun URL manzilini kiriting
url = 'https://jsonplaceholder.typicode.com/posts/1'

# GET so'rovini yuborish
response = requests.get(url)

# Javobni JSON formatida qabul qilish
data = response.json()

# Olingan ma'lumotni ko'rsatish
print(data)
