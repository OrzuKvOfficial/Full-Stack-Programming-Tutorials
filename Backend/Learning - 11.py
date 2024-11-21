import cv2
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

# Funksiya: Video oqimini ko'rsatish
def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        lbl_video.imgtk = img
        lbl_video.configure(image=img)
        lbl_video.after(10, play_video)
    else:
        cap.release()

# GUI oynasi
root = tk.Tk()
root.title("Video Player")

lbl_video = Label(root)
lbl_video.pack()

# Video faylni yuklash
video_path = "video.mp4"  # Video manzilini ko‘rsating
cap = cv2.VideoCapture(video_path)

play_video()
root.mainloop()
