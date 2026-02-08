MANDATORY_FIELDS = [
    "Policy Number",
    "Policyholder Name",
    "Effective Dates",
    "Date",
    "Time",
    "Location",
    "Description",
    "Claimant",
    "Contact Details",
    "Asset Type",
    "Asset ID",
    "Estimated Damage",
    "Claim Type",
    "Attachments",
    "Initial Estimate"
]

def find_missing_fields(extracted_fields):
    missing = []
    for field in MANDATORY_FIELDS:
        if field not in extracted_fields:
            missing.append(field)
    return missing
