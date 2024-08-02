import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# 1. Ma'lumotlarni yuklash
data = load_iris()
X = data.data
y = data.target

# 2. Ma'lumotlarni taqsimlash (train/test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Ma'lumotlarni standartlashtirish
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Modelni yaratish va o'rgatish
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# 5. Modelni sinovdan o'tkazish
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Modelning aniqligi: {accuracy * 100:.2f}%")
