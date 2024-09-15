# Musiqa ma'lumotlari
songs = [
    {"name": "Song A", "genre": "Pop", "length": 3.5},
    {"name": "Song B", "genre": "Rock", "length": 4.2},
    {"name": "Song C", "genre": "Jazz", "length": 5.1},
    {"name": "Song D", "genre": "Pop", "length": 2.9},
    {"name": "Song E", "genre": "Rock", "length": 3.7},
    {"name": "Song F", "genre": "Jazz", "length": 4.5}
]

# Janr bo'yicha filtr
def filter_by_genre(songs, genre):
    return [song for song in songs if song['genre'].lower() == genre.lower()]

# Davomiylik bo'yicha filtr
def filter_by_length(songs, min_length, max_length):
    return [song for song in songs if min_length <= song['length'] <= max_length]

# Musiqalarni saralash
def sort_songs(songs, key):
    return sorted(songs, key=lambda x: x[key])

# Foydalanish:
filtered_songs = filter_by_genre(songs, "Pop")
sorted_songs = sort_songs(filtered_songs, "length")

for song in sorted_songs:
    print(f"Name: {song['name']}, Length: {song['length']} min")
