"""
AI-assisted analysis for the AI Phishing Email Analyzer.
"""


def generate_ai_explanation(
    email_data: dict,
    risk_result: dict,
) -> str:
    """
    Generate a human-readable explanation of the
    phishing analysis results.
    """

    classification = risk_result.get(
        "classification",
        "UNKNOWN"
    )

    score = risk_result.get("score", 0)

    findings = risk_result.get("findings", [])

    if classification == "HIGH RISK / PHISHING":
        explanation = (
            f"The email has a high phishing risk with a "
            f"score of {score}/100. "
        )

    elif classification == "SUSPICIOUS":
        explanation = (
            f"The email contains several suspicious "
            f"indicators and received a risk score of "
            f"{score}/100. "
        )

    else:
        explanation = (
            f"The email has a relatively low risk score "
            f"of {score}/100. "
        )

    if findings:
        explanation += (
            "The analysis identified the following "
            "security indicators: "
        )

        messages = [
            finding.get("message", "")
            for finding in findings
        ]

        explanation += "; ".join(messages) + "."

    else:
        explanation += (
            "No significant phishing indicators were "
            "detected in the supplied email."
        )

    return explanation
