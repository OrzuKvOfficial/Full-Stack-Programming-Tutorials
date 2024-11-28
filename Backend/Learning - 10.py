import json

# JSON faylni yuklash
with open('data.json', 'r') as file:
    data = json.load(file)

# JSON ma'lumotlarni o'qish
print(data)

# JSON ma'lumotlarni o'zgartirish va qayta yozish
data['new_key'] = 'new_value'
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
