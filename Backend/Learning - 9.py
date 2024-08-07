import socket

# Server sozlamalari
HOST = '127.0.0.1'  # Mahalliy host
PORT = 65432        # Ochiq port, siz istalgan raqamni tanlashingiz mumkin

# Socket yaratish
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Serverni host va portga bog'lash
    s.listen()            # Keladigan ulanishlarni tinglash

    print(f'Server {HOST}:{PORT} da ishlamoqda...')

    # Ulanuvchini qabul qilish
    conn, addr = s.accept()  # Yangi ulanishni qabul qilish
    with conn:
        print('Ulanish qabul qilindi:', addr)
        while True:
            data = conn.recv(1024)  # Mijozdan ma'lumot qabul qilish
            if not data:
                break
            print('Qabul qilindi:', data.decode())  # Qabul qilingan ma'lumotni chiqarish
            conn.sendall(data)  # Mijozga qaytarish (echo)
