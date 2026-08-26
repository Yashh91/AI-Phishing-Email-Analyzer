# AI Phishing Email Analyzer

<p align="center">
  <img src="banner.png" alt="AI Phishing Email Analyzer">
</p>

## About

A Python-based cybersecurity tool that analyzes emails for common phishing indicators, calculates a risk score, and provides security recommendations.

## Features

- Email content and header analysis
- Suspicious URL detection
- Phishing keyword detection
- Credential and urgency detection
- Risk scoring
- AI-assisted analysis
- Security report generation

## Screenshots

### Analyzer

![Analyzer Screenshot](screenshots/analyzer.png)

### Phishing Detection Result

![Phishing Detection](screenshots/phishing-result.png)

## Project Structure

AI-Phishing-Email-Analyzer/
│
├── README.md
├── banner.png
├── requirements.txt
├── .gitignore
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── analyzer/
│   │   ├── __init__.py
│   │   ├── email_parser.py
│   │   ├── url_analyzer.py
│   │   ├── text_analyzer.py
│   │   └── risk_engine.py
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   └── ai_analyzer.py
│   │
│   └── reports/
│       ├── __init__.py
│       └── report_generator.py
│
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
│
├── samples/
│   ├── phishing.eml
│   └── legitimate.eml
│
└── screenshots/
    ├── analyzer.png
    └── phishing-result.png

## Installation

git clone https://github.com/YOUR-USERNAME/AI-Phishing-Email-Analyzer.git

cd AI-Phishing-Email-Analyzer

pip install -r requirements.txt

## Run

python -m app.main

## Risk Levels

0–29    LOW RISK
30–59   SUSPICIOUS
60–100  HIGH RISK / PHISHING

## Testing

pytest

## Disclaimer

For educational and authorized defensive-security testing only. The tool does not guarantee that an email is safe or malicious.
