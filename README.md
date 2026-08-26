# 🔐 AI Phishing Email Analyzer

<p align="center">
  <img src="banner.png" alt="AI Phishing Email Analyzer" width="100%">
</p>

<p align="center">
  <b>AI Security • Phishing Detection • Email Threat Analysis</b>
</p>

---

## 📌 About

A Python-based cybersecurity tool that analyzes emails for common phishing indicators, detects suspicious URLs and language patterns, calculates a risk score, and provides security recommendations.

---

## ✨ Features

- 📧 Email header and content analysis
- 🔗 Suspicious URL detection
- ⚠️ Phishing keyword detection
- 🔑 Credential-request detection
- 🚨 Urgency and financial-request detection
- 📊 Risk scoring
- 🤖 AI-assisted analysis
- 📄 Security report generation

---

## 🖥️ Screenshots

### Analyzer

<p align="center">
  <img src="screenshots/analyzer.png" alt="Analyzer Screenshot" width="850">
</p>

### Phishing Detection

<p align="center">
  <img src="screenshots/phishing-result.png" alt="Phishing Detection Result" width="850">
</p>

---

## 📂 Project Structure

```text
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
⚙️ Installation

Clone the repository:

git clone https://github.com/Yashh91/AI-Phishing-Email-Analyzer.git

cd AI-Phishing-Email-Analyzer

Install dependencies:

pip install -r requirements.txt
▶️ Run
python -m app.main

Select:

1. Paste email text
2. Exit

Type END after pasting the email.

📊 Risk Levels
Score	Risk Level
0–29	🟢 Low Risk
30–59	🟡 Suspicious
60–100	🔴 High Risk / Phishing
🧪 Testing
pytest
🛠️ Technologies
Python
BeautifulSoup
Requests
tldextract
Pytest
🔒 Disclaimer

This project is intended for educational and authorized defensive-security testing only. It does not guarantee that an email is safe or malicious.

👤 Author

Yashh91
