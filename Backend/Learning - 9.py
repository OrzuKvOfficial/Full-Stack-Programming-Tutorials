import tkinter as tk

def update_position(event):
    cursor_pos = text.index(tk.INSERT)  # Kursorning pozitsiyasini olish
    pos_label.config(text=f"Kursor pozitsiyasi: {cursor_pos}")

# Oyna yaratish
root = tk.Tk()
root.title("Kursor kuzatish")

# Matn maydoni
text = tk.Text(root, height=10, width=40)
text.pack()

# Pozitsiya ko'rsatish uchun yorliq
pos_label = tk.Label(root, text="Kursor pozitsiyasi: 1.0")
pos_label.pack()

# Kursor harakati kuzatilganda funksiya chaqiriladi
text.bind("<KeyRelease>", update_position)

root.mainloop()
