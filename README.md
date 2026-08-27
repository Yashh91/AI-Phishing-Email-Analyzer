# 🔐 AI Phishing Email Analyzer

##  About

AI Phishing Email Analyzer is a Python-based cybersecurity tool that combines
rule-based analysis with local AI analysis to identify potential phishing emails.

The tool analyzes email content, suspicious URLs, phishing indicators,
social-engineering patterns, and generates a risk assessment with an
AI-generated security explanation.

---

##  Features

-  Email content analysis
-  Suspicious URL detection
-  Phishing keyword detection
-  Credential-request detection
-  Urgency and social-engineering detection
-  Risk scoring
-  AI-powered contextual analysis
-  Local AI analysis using Ollama
-  Security report generation

---

##  AI Analysis

The project uses **Ollama** with the **Qwen3:0.6b** local AI model.

The AI analyzes:

- Phishing likelihood
- Email intent
- Social-engineering indicators
- Suspicious elements
- Potential credential-harvesting attempts
- Overall email context

The AI analysis is combined with rule-based security analysis to provide
a more informative final assessment.

---

##  Screenshots

### Analyzer

<img src="screenshots/analyzer.png" alt="Analyzer Screenshot" width="850">

### Phishing Detection Result

<img src="screenshots/phishing-result.png" alt="Phishing Detection Result" width="850">

---

##  Project Structure

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
```
---
##  Installation

### 1. Clone the Repository
```
git clone https://github.com/Yashh91/AI-Phishing-Email-Analyzer.git
```
```
cd AI-Phishing-Email-Analyzer
```
### 2. Create Virtual Environment
Windows
```
python -m venv .venv
```
Linux / Kali
```
python3 -m venv .venv
```
### 3. Activate Virtual Environment
Windows PowerShell
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
```
.\.venv\Scripts\Activate.ps1
```
Linux / Kali
```
source .venv/bin/activate
```
### 4. Install Python Dependencies
```
python -m pip install -r requirements.txt
```
---
##  Ollama Setup
Ollama is required because the application uses a local AI model
for contextual phishing analysis.
### 1. Install Ollama

Install Ollama on your operating system.

Verify the installation:
```
ollama --version
```
### 2. Download Qwen3 Model
```
ollama pull qwen3:0.6b
```
### 3. Verify the Model
```
ollama list
```
You should see:
qwen3:0.6b
### 4. Test the Model
```
ollama run qwen3:0.6b
```

If the model responds, the AI environment is ready.

---
##  Risk Levels
Score	Risk Level
0–29	 Low Risk
30–59	 Suspicious
60–100	 High Risk / Phishing

---
##  Testing

Run the automated tests:
```
pytest
```
The tests verify core email analysis and risk-scoring functionality.

---
## Disclaimer

This project is intended for educational and authorized defensive-security
testing only.

The analyzer provides an automated security assessment and does not guarantee
that an email is safe or malicious. Always verify suspicious emails through
trusted channels.

---
## Author

Yashh91

---
