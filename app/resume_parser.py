import docx2txt
from PyPDF2 import PdfReader
import os

def extract_text_from_resume(file):
    filename = file.filename
    ext = os.path.splitext(filename)[1].lower()

    if ext == '.pdf':
        reader = PdfReader(file)
        return ' '.join(page.extract_text() for page in reader.pages if page.extract_text())
    elif ext in ['.docx', '.doc']:
        return docx2txt.process(file)
    else:
        return ""
