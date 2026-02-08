MANDATORY_FIELDS = [
    "Policy Number",
    "Policyholder Name",
    "Date of Loss",
    "Location",
    "Description",
    "Claim Type",
    "Estimated Damage"
]

def analyze_fields(extracted):
    missing = []
    analysis_notes = []

    for field in MANDATORY_FIELDS:
        if field not in extracted:
            missing.append(field)

    if "Estimated Damage" in extracted:
        if extracted["Estimated Damage"] <= 0:
            analysis_notes.append("Estimated damage value is invalid.")

    if "Description" in extracted:
        if len(extracted["Description"]) < 15:
            analysis_notes.append("Accident description is too short.")

    return missing, analysis_notes
