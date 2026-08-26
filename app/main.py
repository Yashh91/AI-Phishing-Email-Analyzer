"""
AI Phishing Email Analyzer
Main application entry point.
"""

from app.analyzer.email_parser import parse_email
from app.analyzer.url_analyzer import analyze_urls
from app.analyzer.text_analyzer import analyze_text
from app.analyzer.risk_engine import calculate_risk
from app.ai.ai_analyzer import generate_ai_explanation
from app.reports.report_generator import generate_report, save_report


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
    url_results = analyze_urls(
        email_data.get("urls", [])
    )

    print("[*] Analyzing email text")
    text_results = analyze_text(
        email_data.get("body", "")
    )

    print("[*] Calculating risk score")
    risk_result = calculate_risk(
        url_results,
        text_results,
        email_data
    )

    print("[*] Generating AI explanation")
    ai_explanation = generate_ai_explanation(
        email_data,
        risk_result
    )

    return (
        email_data,
        risk_result,
        ai_explanation
    )


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
                (
                    email_data,
                    risk_result,
                    ai_explanation
                ) = analyze_email(email_text)

                report = generate_report(
                    email_data,
                    risk_result,
                    ai_explanation
                )

                print("\n")
                print(report)

                filename = save_report(report)

                print(
                    f"\n[+] Report saved to: {filename}"
                )

            except Exception as error:
                print(
                    f"\n[ERROR] Analysis failed: {error}\n"
                )

        elif choice == "2":
            print("\nExiting AI Phishing Email Analyzer.")
            break

        else:
            print(
                "\n[!] Invalid option. "
                "Please select 1 or 2.\n"
            )


if __name__ == "__main__":
    main()
