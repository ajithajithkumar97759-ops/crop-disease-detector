from flask import Flask, render_template, request
import os

from utils.image_preprocess import preprocess_image
from utils.prediction import predict_disease

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['image']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    img = preprocess_image(filepath)

    disease, confidence = predict_disease(img)

    return render_template("result.html",
                           disease=disease,
                           confidence=confidence,
                           image_path=filepath)


if __name__ == "__main__":
    app.run(debug=True)