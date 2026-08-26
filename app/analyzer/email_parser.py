"""
Email parser for the AI Phishing Email Analyzer.
"""

import re
from email import policy
from email.parser import Parser
from email.message import Message


URL_PATTERN = re.compile(
    r"https?://[^\s<>\"]+",
    re.IGNORECASE
)


def extract_urls(text: str) -> list[str]:
    """Extract HTTP and HTTPS URLs from text."""

    if not text:
        return []

    urls = URL_PATTERN.findall(text)

    # Remove duplicate URLs while preserving order
    return list(dict.fromkeys(urls))


def extract_body(message: Message) -> str:
    """Extract plain-text body from an email message."""

    if message.is_multipart():
        parts = []

        for part in message.walk():
            content_type = part.get_content_type()

            if content_type == "text/plain":
                try:
                    parts.append(part.get_content())
                except Exception:
                    payload = part.get_payload(decode=True)

                    if payload:
                        parts.append(
                            payload.decode(
                                errors="replace"
                            )
                        )

        return "\n".join(parts)

    try:
        return message.get_content()
    except Exception:
        payload = message.get_payload(decode=True)

        if payload:
            return payload.decode(errors="replace")

    return ""


def extract_attachments(message: Message) -> list[str]:
    """Extract attachment filenames."""

    attachments = []

    for part in message.walk():
        filename = part.get_filename()

        if filename:
            attachments.append(filename)

    return attachments


def parse_email(email_text: str) -> dict:
    """Parse raw email text and return structured information."""

    message = Parser(policy=policy.default).parsestr(email_text)

    sender = message.get("From", "")
    subject = message.get("Subject", "")
    reply_to = message.get("Reply-To", "")

    body = extract_body(message)

    # Analyze both headers and body for URLs
    full_text = f"{email_text}\n{body}"
    urls = extract_urls(full_text)

    attachments = extract_attachments(message)

    return {
        "sender": sender,
        "subject": subject,
        "reply_to": reply_to,
        "body": body,
        "urls": urls,
        "attachments": attachments,
    }
