from datetime import datetime
import pytz

# Joylar va ularning vaqt zonalari
locations = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tashkent": "Asia/Tashkent",
    "Tokyo": "Asia/Tokyo"
}

# Har bir joy uchun hozirgi vaqtni ko'rsatish
for city, timezone in locations.items():
    local_time = datetime.now(pytz.timezone(timezone))
    print(f"{city}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

