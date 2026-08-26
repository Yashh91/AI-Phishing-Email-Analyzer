"""
Risk scoring engine for the AI Phishing Email Analyzer.
"""


def calculate_risk(
    url_results: list[dict],
    text_results: dict,
    email_data: dict,
) -> dict:
    """Calculate the overall phishing risk."""

    score = 0
    findings = []

    # URL risk
    for result in url_results:
        score += result.get("score", 0)

        for indicator in result.get("indicators", []):
            findings.append({
                "severity": "HIGH"
                if result.get("score", 0) >= 30
                else "MEDIUM",
                "message": indicator,
            })

    # Text risk
    score += text_results.get("score", 0)

    for indicator in text_results.get("indicators", []):
        findings.append({
            "severity": indicator["severity"],
            "message": indicator["message"],
        })

    # Attachment check
    attachments = email_data.get("attachments", [])

    if attachments:
        score += 10

        findings.append({
            "severity": "MEDIUM",
            "message": (
                f"Email contains {len(attachments)} attachment(s)"
            ),
        })

    # Limit score
    score = min(score, 100)

    if score >= 60:
        classification = "HIGH RISK / PHISHING"
        recommendation = (
            "Do not click links or provide credentials. "
            "Verify the sender through an independent trusted channel."
        )

    elif score >= 30:
        classification = "SUSPICIOUS"
        recommendation = (
            "Treat the email cautiously and verify the sender "
            "before taking any requested action."
        )

    else:
        classification = "LOW RISK"
        recommendation = (
            "No major phishing indicators were detected. "
            "Continue to verify unexpected messages before acting."
        )

    return {
        "score": score,
        "classification": classification,
        "findings": findings,
        "recommendation": recommendation,
    }
