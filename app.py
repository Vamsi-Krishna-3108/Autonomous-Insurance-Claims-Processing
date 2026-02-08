from flask import Flask, render_template, request
import os

from extractor import extract_text_from_pdf, extract_fields
from analyzer import analyze_fields
from router import route_claim

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        pdf = request.files["pdf"]
        file_path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(file_path)

        text = extract_text_from_pdf(file_path)
        extracted = extract_fields(text)
        missing, notes = analyze_fields(extracted)
        route, reasoning = route_claim(extracted, missing, notes)

        result = {
            "Extracted Fields": extracted,
            "Missing Fields": missing,
            "Analysis Notes": notes,
            "Recommended Route": route,
            "Reasoning": reasoning
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
