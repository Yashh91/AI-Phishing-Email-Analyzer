import ollama


MODEL = "qwen3:0.6b"


def generate_ai_explanation(email_text, risk_score):
    prompt = f"""
You are a cybersecurity email analysis assistant.

Analyze the following email for phishing.

Current rule-based risk score: {risk_score}/100

Email:
{email_text}

Provide:

1. Phishing likelihood: Low, Medium, or High
2. Intent of the email
3. Social engineering indicators
4. Suspicious elements
5. Short explanation

Consider the rule-based risk score, but perform your own contextual analysis.

Keep the response concise and focused on defensive security analysis.
"""

    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI analysis failed: {e}"
