import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email ma'lumotlari
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@example.com"
password = "your_password"

# Email xabari tayyorlash
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Email Subject"

# Email mazmuni
body = "Bu emailning mazmuni."
message.attach(MIMEText(body, 'plain'))

# SMTP serverga ulanish va email yuborish
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # TLS (Transport Layer Security) ni yoqish
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email muvaffaqiyatli yuborildi.")
except Exception as e:
    print(f"Xato yuz berdi: {e}")
finally:
    server.quit()
