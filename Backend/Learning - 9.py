import cv2

# Yuzni aniqlash uchun OpenCV Haar Cascade modelini yuklash
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Kamerani yoqish
cap = cv2.VideoCapture(0)

while True:
    # Videoni oqish
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yuzni aniqlash
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        # Yuz atrofiga to‘g‘ri to‘rtburchak chizish
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Yuz sohasidan faqat og‘iz qismini qidirish
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Tabassumni aniqlash
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        
        for (sx, sy, sw, sh) in smiles:
            # Agar tabassum bo'lsa, uni ifodalash
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
            
            # "Smile detected!" matnini ko‘rsatish
            cv2.putText(frame, 'Smile detected!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Natijani ko‘rsatish
    cv2.imshow('Smile Detector', frame)
    
    # 'q' tugmasini bosish bilan chiqish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerani o'chirish va oynani yopish
cap.release()
cv2.destroyAllWindows()
