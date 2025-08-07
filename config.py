# config.py

import os

class Config:
    SECRET_KEY = 'supersecretkey'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
