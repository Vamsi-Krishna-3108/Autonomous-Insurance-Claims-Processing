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
        # Policy Information
        "Policy Number": r"Policy Number[:\s]*([A-Z0-9-]+)",
        "Policyholder Name": r"Policyholder Name[:\s]*(.+)",
        "Effective Dates": r"Effective Dates[:\s]*([\d/]+\s*-\s*[\d/]+)",

        # Incident Information
        "Date": r"Date of Loss[:\s]*([\d/]+)",
        "Time": r"Time of Loss[:\s]*([\d:]+)",
        "Location": r"Location of Loss[:\s]*(.+)",
        "Description": r"Description[:\s]*(.+)",

        # Involved Parties
        "Claimant": r"Claimant[:\s]*(.+)",
        "Third Parties": r"Third Parties[:\s]*(.+)",
        "Contact Details": r"Contact Details[:\s]*(.+)",

        # Asset Details
        "Asset Type": r"Asset Type[:\s]*(.+)",
        "Asset ID": r"Asset ID[:\s]*(.+)",
        "Estimated Damage": r"Estimated Damage[:\s]*\$?([\d,]+)",

        # Other Mandatory Fields
        "Claim Type": r"Claim Type[:\s]*(injury|vehicle|property)",
        "Attachments": r"Attachments[:\s]*(.+)",
        "Initial Estimate": r"Initial Estimate[:\s]*\$?([\d,]+)"
    }

    extracted = {}
    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).strip()
            if field in ["Estimated Damage", "Initial Estimate"]:
                value = int(value.replace(",", ""))
            extracted[field] = value

    return extracted
