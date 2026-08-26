# 🔐 AI Phishing Email Analyzer

AI Security • Phishing Detection • Email Threat Analysis

Author: Yashh91

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📌 About

A Python-based cybersecurity tool that analyzes emails for common phishing indicators, detects suspicious URLs and language patterns, calculates a risk score, and provides security recommendations.

## ✨ Features

• Email header and content analysis
• Suspicious URL detection
• Phishing keyword detection
• Credential-request detection
• Urgency and financial-request detection
• Risk scoring
• AI-assisted analysis
• Security report generation

## 🖥️ Screenshots

### Analyzer

![Analyzer Screenshot](screenshots/analyzer.png)

### Phishing Detection Result

![Phishing Detection Result](screenshots/phishing-result.png)

## 📂 Project Structure

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

## ⚙️ Installation

git clone https://github.com/Yashh91/AI-Phishing-Email-Analyzer.git
cd AI-Phishing-Email-Analyzer
pip install -r requirements.txt

## ▶️ Run

python -m app.main

## 📊 Risk Levels

0–29    → 🟢 Low Risk
30–59   → 🟡 Suspicious
60–100  → 🔴 High Risk / Phishing

## 🧪 Testing

pytest

## 🛠️ Technologies

• Python
• BeautifulSoup
• Requests
• tldextract
• Pytest

## 🔒 Disclaimer

This project is intended for educational and authorized defensive-security testing only. It does not guarantee that an email is safe or malicious.

## 👤 Author

Yashh91
