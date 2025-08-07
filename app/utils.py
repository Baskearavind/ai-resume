import os

def create_upload_folder(path='uploads'):
    if not os.path.exists(path):
        os.makedirs(path)
