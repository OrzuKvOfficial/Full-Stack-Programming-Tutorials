import cv2
import mediapipe as mp

# Mediapipe yuzni aniqlash modeli
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Kamera orqali video oqimini olish
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Kameradan oqib olishning imkoni yo'q")
            break

        # BGR tasvirni RGB ga aylantirish
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)

        # Yuzni aniqlash
        if results.detections:
            for detection in results.detections:
                # Yuzni rasmga chizish
                mp_drawing.draw_detection(image, detection)

                # Agar kerak bo'lsa, bu yerda ko'zoynakni aniqlash uchun algoritm qo'shishingiz mumkin
                # Masalan, ko'zning holatini tahlil qilish va ko'zoynak belgilarini qidirish
                # Shuningdek, ko'zoynak taqmaganligini aniqlaganda eslatish xabarini chiqarish

        # Oynada tasvirni ko'rsatish
        cv2.imshow('Camera', image)

        # Qandaydir tugmani bosganda chiqib ketish
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
