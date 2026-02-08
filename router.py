def route_claim(extracted, missing_fields, analysis_notes=None):
    description = extracted.get("Description", "").lower()
    claim_type = extracted.get("Claim Type", "").lower()
    estimated_damage = extracted.get("Estimated Damage", 0)

    # Rule 1: Missing mandatory fields
    if missing_fields:
        return (
            "Manual review",
            "One or more mandatory fields are missing."
        )

    # Rule 2: Fraud keywords
    if any(word in description for word in ["fraud", "inconsistent", "staged"]):
        return (
            "Investigation Flag",
            "Claim description contains keywords indicating potential fraud."
        )

    # Rule 3: Injury claims
    if claim_type == "injury":
        return (
            "Specialist Queue",
            "Injury-related claims require specialist handling."
        )

    # Rule 4: Fast-track
    if estimated_damage < 25000:
        return (
            "Fast-track",
            "Estimated damage is below 25,000."
        )

    return (
        "Manual review",
        "Claim does not meet fast-track conditions."
    )
