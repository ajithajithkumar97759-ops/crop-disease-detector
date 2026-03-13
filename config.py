import os

class Config:
    SECRET_KEY = "secretkey"
    UPLOAD_FOLDER = os.path.join("static", "uploads")
    