# 🧾 Autonomous Insurance Claims Processing Agent

## 📌 Overview

This project is a **full-stack autonomous insurance claims processing system** built using **Python and Flask**.
It processes **FNOL (First Notice of Loss) PDF documents**, extracts structured claim information, validates completeness, and automatically routes claims based on predefined business rules.

The system is **fully offline**, does **not require any API keys**, and uses **rule-based intelligence** to ensure transparency and explainability.

---

## 🎯 Problem Statement

Build a lightweight agent that:

* Extracts key fields from FNOL documents
* Identifies missing or inconsistent information
* Classifies and routes claims to the correct workflow
* Provides a clear explanation for routing decisions

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **PDF Processing:** pdfplumber
* **Frontend:** HTML, Bootstrap 5, Jinja2
* **Output Format:** JSON

---

## 📂 Project Structure

```
insurance-claims-processing-agent/
│
├── app.py                 # Flask application
├── extractor.py           # PDF to text & field extraction
├── analyzer.py            # Mandatory field validation
├── router.py              # Claim routing logic
│
├── templates/
│   └── index.html         # Bootstrap UI
│
├── uploads/               # Uploaded FNOL PDFs
├── last_result.json       # Generated JSON output
├── requirements.txt
└── README.md
```

---

## 📄 Fields Extracted

### 🔹 Policy Information

* Policy Number
* Policyholder Name
* Effective Dates

### 🔹 Incident Information

* Date
* Time
* Location
* Description

### 🔹 Involved Parties

* Claimant
* Third Parties
* Contact Details

### 🔹 Asset Details

* Asset Type
* Asset ID
* Estimated Damage

### 🔹 Other Mandatory Fields

* Claim Type
* Attachments
* Initial Estimate

---

## 🚦 Routing Rules

| Condition                                              | Route              |
| ------------------------------------------------------ | ------------------ |
| Estimated Damage < 25,000                              | Fast-track         |
| Any mandatory field missing                            | Manual review      |
| Description contains “fraud”, “inconsistent”, “staged” | Investigation Flag |
| Claim Type = injury                                    | Specialist Queue   |

---

## 📤 Output Format (JSON)

```json
{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}
```

A **Download JSON** button is available in the UI to export this result.

---

## 🖥️ User Interface

* Upload FNOL PDF through browser
* View extracted fields in a structured format
* See missing fields and routing decision
* Download JSON output for downstream systems

---

## ▶️ How to Run Locally

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Application

```bash
python app.py
```

### 3️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧪 Test Scenarios Included

* ✅ Complete FNOL → Fast-track
* 🚩 Fraud FNOL → Investigation Flag
* 🏥 Injury FNOL → Specialist Queue
* ⚠️ Missing Fields FNOL → Manual Review

---

## 💡 Key Design Highlights

* Fully offline (no API keys)
* Rule-based, explainable decision logic
* Modular architecture
* Easy to extend with AI/LLM in the future
* Enterprise-style workflow automation

---

## 🎤 Interview Explanation (Short)

> “I built a full-stack Flask application that processes FNOL PDFs, extracts structured claim data, validates mandatory fields, and automatically routes insurance claims with clear reasoning using rule-based logic.”

---

## 🚀 Future Enhancements

* Fraud confidence scoring
* Multi-PDF batch processing
* Role-based access (Agent / Reviewer)
* Cloud deployment
* LLM-based reasoning (optional)

---

## 📜 License

I used the MIT License to allow free use, modification, and distribution while keeping liability protection.

Just tell me — happy to help 👌
