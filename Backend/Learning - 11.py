import hashlib

def fayl_hashini_olish(fayl_nomi):
    hash_obj = hashlib.sha256()
    with open(fayl_nomi, "rb") as fayl:
        for qism in iter(lambda: fayl.read(4096), b""):
            hash_obj.update(qism)
    return hash_obj.hexdigest()

# Hashni tekshirish
fayl_nomi = "tekshir_fayl.txt"
hashi = fayl_hashini_olish(fayl_nomi)
print("Faylning SHA-256 hash qiymati:", hashi)
