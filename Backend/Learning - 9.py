import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Rasmni yuklash va oldindan ishlash
img = image.load_img('rasm_path.jpg', target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# Tayyor modelni yuklash va bashorat qilish
model = tf.keras.applications.MobileNetV2(weights='imagenet')
preds = model.predict(img_array)
