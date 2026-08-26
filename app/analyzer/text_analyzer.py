"""
Text analyzer for detecting common phishing indicators.
"""

import re


URGENCY_KEYWORDS = {
    "urgent",
    "immediately",
    "immediate",
    "as soon as possible",
    "within 24 hours",
    "act now",
    "final warning",
    "action required",
    "account suspended",
    "account will be closed",
}


CREDENTIAL_KEYWORDS = {
    "password",
    "username",
    "login",
    "sign in",
    "verification code",
    "otp",
    "credentials",
    "security code",
}


FINANCIAL_KEYWORDS = {
    "payment",
    "invoice",
    "bank account",
    "credit card",
    "debit card",
    "refund",
    "transfer",
    "wire transfer",
}


def find_keywords(text: str, keywords: set[str]) -> list[str]:
    """Find security-related keywords in text."""

    text_lower = text.lower()

    found = []

    for keyword in keywords:
        if keyword in text_lower:
            found.append(keyword)

    return sorted(found)


def analyze_text(text: str) -> dict:
    """Analyze email text for phishing indicators."""

    if not text:
        return {
            "urgency": [],
            "credentials": [],
            "financial": [],
            "score": 0,
            "indicators": [],
        }

    urgency = find_keywords(text, URGENCY_KEYWORDS)
    credentials = find_keywords(text, CREDENTIAL_KEYWORDS)
    financial = find_keywords(text, FINANCIAL_KEYWORDS)

    indicators = []
    score = 0

    if urgency:
        score += min(len(urgency) * 5, 15)

        indicators.append({
            "type": "urgency",
            "severity": "MEDIUM",
            "message": (
                "Urgency language detected: "
                + ", ".join(urgency)
            ),
        })

    if credentials:
        score += min(len(credentials) * 10, 30)

        indicators.append({
            "type": "credentials",
            "severity": "HIGH",
            "message": (
                "Credential-related language detected: "
                + ", ".join(credentials)
            ),
        })

    if financial:
        score += min(len(financial) * 8, 20)

        indicators.append({
            "type": "financial",
            "severity": "MEDIUM",
            "message": (
                "Financial-related language detected: "
                + ", ".join(financial)
            ),
        })

    return {
        "urgency": urgency,
        "credentials": credentials,
        "financial": financial,
        "score": min(score, 100),
        "indicators": indicators,
    }
