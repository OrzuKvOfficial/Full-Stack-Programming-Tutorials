# Fayl ichida shubhali buyruqlarni qidirish
def zararli_kodni_tekshirish(fayl_nomi):
    shubhali_sozlar = ["eval(", "exec(", "import os", "subprocess", "open(", "socket"]
    zararli = False
    
    with open(fayl_nomi, "r", encoding="utf-8") as fayl:
        for qator in fayl:
            if any(soz in qator for soz in shubhali_sozlar):
                zararli = True
                print("Zararli kod topildi:", qator.strip())
    
    if zararli:
        print("Faylda zararli kod topildi.")
    else:
        print("Fayl xavfsiz.")
        
# Faylni tekshirish
zararli_kodni_tekshirish("tekshir_fayl.txt")
