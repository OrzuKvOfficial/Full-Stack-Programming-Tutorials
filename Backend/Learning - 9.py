import platform

# Tizim nomi va versiyasi
print(f"System: {platform.system()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")

# Protsessor ma'lumotlari
print(f"Processor: {platform.processor()}")

# Tizim me'morchiligi (32-bit yoki 64-bit)
print(f"Architecture: {platform.architecture()[0]}")
