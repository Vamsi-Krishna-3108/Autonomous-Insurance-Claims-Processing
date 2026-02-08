def route_claim(extracted, missing, notes):
    description = extracted.get("Description", "").lower()

    if missing:
        return (
            "Manual Review",
            "Claim routed to manual review because mandatory fields are missing."
        )

    if any(word in description for word in ["fraud", "staged", "inconsistent"]):
        return (
            "Investigation Flag",
            "Claim description contains keywords indicating potential fraud."
        )

    if extracted.get("Claim Type") == "injury":
        return (
            "Specialist Queue",
            "Injury-related claims require specialist assessment."
        )

    if extracted.get("Estimated Damage", 0) < 25000:
        return (
            "Fast-track",
            "Estimated damage is below 25,000, eligible for fast-track processing."
        )

    return (
        "Manual Review",
        "Claim does not meet fast-track criteria and requires human verification."
    )
