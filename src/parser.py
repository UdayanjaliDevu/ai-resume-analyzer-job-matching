import os
import pdfplumber
import docx


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        raise Exception(f"Error reading PDF: {e}")
    return text


def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        raise Exception(f"Error reading DOCX: {e}")
    return text


def read_resume(file_path):
    """
    Reads resume file and returns raw text
    Supports: .txt, .pdf, .docx
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = file_path.split(".")[-1].lower()

    if ext == "txt":
        text = read_txt(file_path)

    elif ext == "pdf":
        text = read_pdf(file_path)

    elif ext == "docx":
        text = read_docx(file_path)

    else:
        raise ValueError("Unsupported file format")

    if not text or not text.strip():
        raise ValueError("File is empty or unreadable")

    return text