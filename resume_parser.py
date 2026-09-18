import pdfplumber
from docx import Document
import re


def read_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def read_docx(file_path):
    doc = Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_name(text):

    lines = text.split("\n")

    if len(lines) > 0:
        return lines[0]

    return "Not Found"


def extract_email(text):

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text,
    )

    if email:
        return email[0]

    return "Not Found"


def extract_phone(text):

    phone = re.findall(
        r"\+?\d[\d\s\-]{8,15}",
        text,
    )

    if phone:
        return phone[0]

    return "Not Found"
def extract_skills(text):

    skills = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "MySQL",
        "SQLite",
        "Pandas",
        "NumPy",
        "TensorFlow",
        "Keras",
        "Machine Learning",
        "Deep Learning",
        "Tkinter",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Git",
        "GitHub",
        "MongoDB",
        "Flask",
        "Django"
    ]

    found = []

    text = text.lower()

    for skill in skills:

        if skill.lower() in text:
            found.append(skill)

    return found


def parse_resume(file_path):

    if file_path.endswith(".pdf"):
        text = read_pdf(file_path)

    elif file_path.endswith(".docx"):
        text = read_docx(file_path)

    else:
        return None

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "resume_text": text,
    }

    return data