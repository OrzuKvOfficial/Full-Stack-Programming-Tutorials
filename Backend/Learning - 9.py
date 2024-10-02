import win32print

def check_printers():
    # Kompyuterga ulangan printerlar ro'yxatini olish
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

    if printers:
        print("Quyidagi printerlar ulangan:")
        for printer in printers:
            print(f"Printer nomi: {printer[2]}")
    else:
        print("Printerlar topilmadi.")

check_printers()
