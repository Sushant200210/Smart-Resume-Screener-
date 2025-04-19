# utils/pdf_parser.py
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(file):
    """Handle both file paths (str) and Streamlit UploadedFile objects"""
    text = ""
    
    if isinstance(file, str):  # Case 1: It's a file path string
        with open(file, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    
    else:  # Case 2: It's a Streamlit UploadedFile object
        reader = PyPDF2.PdfReader(BytesIO(file.read()))
        for page in reader.pages:
            text += page.extract_text() or ""
    
    return text.strip() 

