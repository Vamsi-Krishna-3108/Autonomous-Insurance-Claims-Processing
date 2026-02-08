from flask import Flask, render_template, request, send_file
import os, json

from extractor import extract_text_from_pdf, extract_fields
from analyzer import find_missing_fields
from router import route_claim

app = Flask(__name__)
app.secret_key = "claims-secret-key"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

LAST_RESULT_PATH = "last_result.json"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        pdf = request.files["pdf"]
        file_path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(file_path)

        text = extract_text_from_pdf(file_path)
        extracted = extract_fields(text)
        missing = find_missing_fields(extracted)

        route, reasoning = route_claim(extracted, missing, [])

        result = {
            "extractedFields": extracted,
            "missingFields": missing,
            "recommendedRoute": route,
            "reasoning": reasoning
        }

        with open(LAST_RESULT_PATH, "w") as f:
            json.dump(result, f, indent=4)

    return render_template("index.html", result=result)


@app.route("/download-json")
def download_json():
    return send_file(
        LAST_RESULT_PATH,
        as_attachment=True,
        download_name="claim_analysis_result.json"
    )


if __name__ == "__main__":
    app.run(debug=True)
