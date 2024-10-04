# Kerakli kutubxonalarni import qilish
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Ma'lumotlar to'plami (o'zingizning ma'lumotlaringiz bo'lishi mumkin)
X = np.array([[1], [2], [3], [4], [5]])  # Mustaqil o'zgaruvchi
y = np.array([1, 4, 9, 16, 25])          # Bog'liq o'zgaruvchi (sodda kvadrat funktsiya)

# Ma'lumotlarni trenirovka va test to'plamlariga ajratish
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model yaratish va trenirovka qilish
model = LinearRegression()
model.fit(X_train, y_train)

# Test ma'lumotlari bo'yicha prognoz qilish
y_pred = model.predict(X_test)

# Natijalarni chop qilish
print("Prognozlangan natijalar:", y_pred)
