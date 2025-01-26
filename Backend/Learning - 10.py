from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim

def get_country_time(country_name):
    try:
        # Geolokatsiya obyekti
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(country_name)
        
        if not location:
            return f"{country_name} uchun joylashuv topilmadi."
        
        # Vaqt zonasi aniqlash
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)
        
        if not timezone_str:
            return f"{country_name} uchun vaqt zonasi topilmadi."
        
        # Hozirgi vaqtni olish
        timezone = pytz.timezone(timezone_str)
        country_time = datetime.now(timezone)
        
        return f"{country_name} vaqti: {country_time.strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Xato yuz berdi: {e}"

# Foydalanuvchidan davlat nomini so'rash
country = input("Davlat nomini kiriting: ")
print(get_country_time(country))
