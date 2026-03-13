from flask import Flask, render_template, request
from utils.prediction import predict_disease
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["image"]
        filepath = os.path.join("static", file.filename)
        file.save(filepath)

        disease, confidence = predict_disease(filepath)
        result = f"{disease} ({confidence}%)"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)