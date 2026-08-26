"""
AI Phishing Email Analyzer
Main application entry point.
"""

from app.analyzer.email_parser import parse_email
from app.analyzer.url_analyzer import analyze_urls
from app.analyzer.text_analyzer import analyze_text
from app.analyzer.risk_engine import calculate_risk


def print_banner():
    print("=" * 60)
    print("              AI PHISHING EMAIL ANALYZER")
    print("=" * 60)
    print()


def get_email_text():
    print("-" * 60)
    print("Paste the email below.")
    print("Type END on a new line when finished.")
    print("-" * 60)

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return "\n".join(lines)


def analyze_email(email_text):
    print("\nAnalyzing email...")
    print("[*] Parsing email")
    
    email_data = parse_email(email_text)

    print("[*] Analyzing URLs")
    url_results = analyze_urls(email_data.get("urls", []))

    print("[*] Analyzing email text")
    text_results = analyze_text(email_data.get("body", ""))

    print("[*] Calculating risk score")
    risk_result = calculate_risk(
        url_results,
        text_results,
        email_data
    )

    return email_data, url_results, text_results, risk_result


def display_result(email_data, url_results, text_results, risk_result):
    print("\n")
    print("=" * 60)
    print("                PHISHING ANALYSIS REPORT")
    print("=" * 60)

    print(f"\nSender         : {email_data.get('sender', 'Unknown')}")
    print(f"Subject        : {email_data.get('subject', 'Unknown')}")

    print("\n" + "-" * 60)
    print("RISK ASSESSMENT")
    print("-" * 60)

    print(f"Risk Score     : {risk_result['score']}/100")
    print(f"Classification : {risk_result['classification']}")

    print("\n" + "-" * 60)
    print("DETECTED INDICATORS")
    print("-" * 60)

    findings = risk_result.get("findings", [])

    if not findings:
        print("[INFO] No significant phishing indicators detected.")
    else:
        for finding in findings:
            print(f"[{finding['severity']}] {finding['message']}")

    print("\n" + "-" * 60)
    print("RECOMMENDATION")
    print("-" * 60)

    print(risk_result.get(
        "recommendation",
        "Review the email carefully before taking any action."
    ))

    print("\n" + "=" * 60)


def main():
    print_banner()

    while True:
        print("1. Paste email text")
        print("2. Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            email_text = get_email_text()

            if not email_text.strip():
                print("\n[!] No email content provided.\n")
                continue

            try:
                email_data, url_results, text_results, risk_result = (
                    analyze_email(email_text)
                )

                display_result(
                    email_data,
                    url_results,
                    text_results,
                    risk_result
                )

            except Exception as error:
                print(f"\n[ERROR] Analysis failed: {error}\n")

        elif choice == "2":
            print("\nExiting AI Phishing Email Analyzer.")
            break

        else:
            print("\n[!] Invalid option. Please select 1 or 2.\n")


if __name__ == "__main__":
    main()
