from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

np.set_printoptions(suppress=True)
model = load_model("keras_Model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

def preprocess_image(image_path):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return None
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data

def predict_image(image_path):
    data = preprocess_image(image_path)
    if data is None:
        return
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]
    print(f"Image: {image_path}")
    print(f"Class: {class_name}")
    print(f"Confidence Score: {confidence_score * 100:.2f}%")
    print('--------------------------')
image_path1 = input("Enter full path to first image: ").strip().strip('"').strip("'")
image_path2 = input("Enter full path to second image: ").strip().strip('"').strip("'")
predict_image(image_path1)
predict_image(image_path2)

#paths :
#C:\Users\mawad\Downloads\KATtest1.jpeg
#C:\Users\mawad\Downloads\PEETAtest2.jpeg