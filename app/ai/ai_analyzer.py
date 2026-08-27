import ollama


MODEL = "qwen3:0.6b"


def analyze_email_with_ai(email_text):
    prompt = f"""
You are a cybersecurity email analysis assistant.

Analyze the following email for phishing.

Email:
{email_text}

Return:

1. Phishing likelihood: Low, Medium, or High
2. Intent: What is the sender trying to make the user do?
3. Social engineering indicators
4. Suspicious elements
5. Short explanation

Do not provide instructions for attacking anyone.
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
