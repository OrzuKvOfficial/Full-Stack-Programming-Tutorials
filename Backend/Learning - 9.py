from PIL import Image

# Rasm nomini id sifatida belgilaymiz
rasm_id = "image123.jpg"

# Rasmni yuklash
rasm = Image.open(rasm_id)

# Rasmni o'zgartirish: masalan, o'lchamini kichiklashtirish
rasm = rasm.resize((200, 200))

# Rasmni saqlash
rasm.save("new_" + rasm_id)
