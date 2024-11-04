import geocoder

# IP manzil orqali hozirgi joylashuvni aniqlash
g = geocoder.ip('me')

if g.ok:
    print("Sizning joylashuvingiz:")
    print(f"Shahar: {g.city}")
    print(f"Mamlakat: {g.country}")
    print(f"Koordinatalar: {g.latlng}")
else:
    print("Joylashuv aniqlanmadi.")
