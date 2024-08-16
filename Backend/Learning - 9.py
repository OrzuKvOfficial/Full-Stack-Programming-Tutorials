import cv2

# Kamerani ulash
cap = cv2.VideoCapture(0)

while True:
    # Video oqimidan ramkalarni o'qing
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Tasvirni ko'rsatish
    cv2.imshow('Kamera', frame)
    
    # Agar 'q' tugmasi bosilsa, chiqish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerani yopish va barcha oynalarni o'chirish
cap.release()
cv2.destroyAllWindows()
