# utils/prediction.py
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Uncomment next line if model ready
# model = load_model("model/plant_disease_model.h5")

class_names = [
    "Healthy",
    "Leaf Blight",
    "Brown Spot",
    "Powdery Mildew",
    "Rust",
    "Bacterial Spot"
]

def predict_disease(img):
    # Test function for now
    return "Test Disease", 99

    # Real prediction code (uncomment when model ready)
    # img_array = np.array(img)
    # img_array = np.expand_dims(img_array, axis=0)
    # prediction = model.predict(img_array)
    # predicted_class = class_names[np.argmax(prediction)]
    # confidence = round(100 * np.max(prediction), 2)
    # return predicted_class, confidence