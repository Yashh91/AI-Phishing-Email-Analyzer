"""
Tests for the AI Phishing Email Analyzer.
"""

from app.analyzer.email_parser import parse_email
from app.analyzer.url_analyzer import analyze_urls
from app.analyzer.text_analyzer import analyze_text
from app.analyzer.risk_engine import calculate_risk


def test_email_parser():
    email = """From: security@example.com
Subject: Test Email

This is a test email.
https://example.com/login
"""

    result = parse_email(email)

    assert result["sender"] == "security@example.com"
    assert result["subject"] == "Test Email"
    assert "https://example.com/login" in result["urls"]


def test_url_analyzer():
    urls = [
        "http://192.168.1.10/login"
    ]

    results = analyze_urls(urls)

    assert len(results) == 1
    assert results[0]["suspicious"] is True
    assert results[0]["score"] > 0


def test_text_analyzer():
    text = """
    Urgent! Your account is suspended.
    Please provide your password immediately.
    """

    result = analyze_text(text)

    assert len(result["urgency"]) > 0
    assert len(result["credentials"]) > 0
    assert result["score"] > 0


def test_risk_engine():
    email_data = {
        "sender": "security@example.com",
        "subject": "Test",
        "attachments": []
    }

    url_results = [
        {
            "url": "http://192.168.1.10/login",
            "suspicious": True,
            "score": 40,
            "indicators": [
                "URL uses an IP address"
            ]
        }
    ]

    text_results = {
        "score": 30,
        "indicators": [
            {
                "severity": "HIGH",
                "message": "Credential-related language detected"
            }
        ]
    }

    result = calculate_risk(
        url_results,
        text_results,
        email_data
    )

    assert result["score"] == 70
    assert result["classification"] == "HIGH RISK / PHISHING"
    assert len(result["findings"]) > 0
