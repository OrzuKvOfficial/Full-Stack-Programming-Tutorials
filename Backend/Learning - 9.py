import cv2

# Kamerani ochish (0 - bu kompyuterdagi birinchi kamera)
cap = cv2.VideoCapture(0)

while True:
    # Kameradan tasvirni o'qish
    ret, frame = cap.read()

    # Tasvirni oynada ko'rsatish
    cv2.imshow('Camera', frame)

    # 'q' tugmasini bosish orqali dasturdan chiqish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerani yopish va barcha oynalarni yo'q qilish
cap.release()
cv2.destroyAllWindows()
