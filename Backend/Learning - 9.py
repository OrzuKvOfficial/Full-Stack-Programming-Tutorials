# Savdo jadvalining hisob mashinasi

def savdo_hisob_mashinasi():
    jami = 0
    mahsulotlar_soni = int(input("Nechta mahsulot sotib olishni xohlaysiz? "))

    for i in range(mahsulotlar_soni):
        mahsulot_nomi = input(f"{i+1}-mahsulot nomi: ")
        narx = float(input(f"{mahsulot_nomi}ning narxi (so'm): "))
        miqdor = int(input(f"{mahsulot_nomi} miqdori: "))
        umumiy = narx * miqdor
        jami += umumiy
        print(f"{mahsulot_nomi} umumiy narxi: {umumiy} so'm\n")

    print(f"Sizning umumiy xarid summangiz: {jami} so'm")

savdo_hisob_mashinasi()
