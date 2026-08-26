"""
Security report generator for the AI Phishing Email Analyzer.
"""


def generate_report(
    email_data: dict,
    risk_result: dict,
    ai_explanation: str = "",
) -> str:
    """Generate a text-based phishing analysis report."""

    sender = email_data.get("sender", "Unknown")
    subject = email_data.get("subject", "Unknown")

    score = risk_result.get("score", 0)
    classification = risk_result.get(
        "classification",
        "UNKNOWN"
    )

    findings = risk_result.get("findings", [])

    recommendation = risk_result.get(
        "recommendation",
        "Review the email carefully before taking action."
    )

    lines = []

    lines.append("=" * 60)
    lines.append("             AI PHISHING ANALYSIS REPORT")
    lines.append("=" * 60)

    lines.append("")
    lines.append("EMAIL INFORMATION")
    lines.append("-" * 60)
    lines.append(f"Sender         : {sender}")
    lines.append(f"Subject        : {subject}")

    lines.append("")
    lines.append("RISK ASSESSMENT")
    lines.append("-" * 60)
    lines.append(f"Risk Score     : {score}/100")
    lines.append(f"Classification : {classification}")

    lines.append("")
    lines.append("DETECTED INDICATORS")
    lines.append("-" * 60)

    if findings:
        for finding in findings:
            severity = finding.get("severity", "INFO")
            message = finding.get("message", "")

            lines.append(
                f"[{severity}] {message}"
            )
    else:
        lines.append(
            "[INFO] No significant phishing indicators detected."
        )

    lines.append("")
    lines.append("AI ANALYSIS")
    lines.append("-" * 60)

    if ai_explanation:
        lines.append(ai_explanation)
    else:
        lines.append(
            "AI explanation is not available."
        )

    lines.append("")
    lines.append("RECOMMENDATION")
    lines.append("-" * 60)
    lines.append(recommendation)

    lines.append("")
    lines.append("=" * 60)

    return "\n".join(lines)


def save_report(report: str, filename: str = "phishing_report.txt"):
    """Save the generated report to a text file."""

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    return filename
