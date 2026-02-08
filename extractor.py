import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_fields(text):
    patterns = {
        "Policy Number": r"POLICY NUMBER[:\s]*([A-Z0-9]+)",
        "Policyholder Name": r"NAME OF INSURED.*?:\s*(.+)",
        "Date of Loss": r"DATE OF LOSS.*?:\s*([\d/]+)",
        "Location": r"LOCATION OF LOSS.*?:\s*(.+)",
        "Description": r"DESCRIPTION OF ACCIDENT.*?:\s*(.+)",
        "Estimated Damage": r"ESTIMATE AMOUNT[:\s]*\$?([\d,]+)",
        "Claim Type": r"(injury|vehicle|property)"
    }

    extracted = {}
    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).strip()
            if field == "Estimated Damage":
                value = int(value.replace(",", ""))
            extracted[field] = value

    return extracted
