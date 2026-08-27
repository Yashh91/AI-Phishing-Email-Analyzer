import ollama


MODEL = "qwen3:0.6b"


def generate_ai_explanation(email_text):
    prompt = f"""
You are a cybersecurity email analysis assistant.

Analyze the following email for phishing.

Email:
{email_text}

Provide:

1. Phishing likelihood: Low, Medium, or High
2. Intent of the email
3. Social engineering indicators
4. Suspicious elements
5. Short explanation

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
