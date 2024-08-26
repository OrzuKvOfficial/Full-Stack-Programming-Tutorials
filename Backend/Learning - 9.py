from PIL import Image, ImageEnhance

# Tasvirni ochish
image = Image.open("rasm.png")

# Rangni oshirish yoki kamaytirish (1.0 normal, 0.0 rang yo'q, 2.0 rang ikki barobar kuchli)
enhancer = ImageEnhance.Color(image)
image_enhanced = enhancer.enhance(1.5)

# Natijani saqlash
image_enhanced.save("rasm_enhanced.png")
image_enhanced.show()
