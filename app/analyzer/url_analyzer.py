"""
URL security analyzer for the AI Phishing Email Analyzer.
"""

import ipaddress
from urllib.parse import urlparse

import tldextract


SUSPICIOUS_KEYWORDS = {
    "login",
    "signin",
    "verify",
    "verification",
    "secure",
    "account",
    "update",
    "password",
    "confirm",
}


def is_ip_address(hostname: str) -> bool:
    """Check whether a hostname is an IP address."""

    if not hostname:
        return False

    try:
        ipaddress.ip_address(hostname)
        return True
    except ValueError:
        return False


def analyze_url(url: str) -> dict:
    """Analyze a single URL for common phishing indicators."""

    result = {
        "url": url,
        "suspicious": False,
        "score": 0,
        "indicators": [],
    }

    try:
        parsed = urlparse(url)

        hostname = parsed.hostname or ""
        hostname = hostname.lower()

        if not hostname:
            result["suspicious"] = True
            result["score"] += 20
            result["indicators"].append(
                "Invalid or missing hostname"
            )
            return result

        # HTTP instead of HTTPS
        if parsed.scheme.lower() == "http":
            result["score"] += 10
            result["indicators"].append(
                "URL does not use HTTPS"
            )

        # Direct IP address
        if is_ip_address(hostname):
            result["score"] += 20
            result["indicators"].append(
                "URL uses an IP address instead of a domain"
            )

        # Suspicious keywords
        url_lower = url.lower()

        matched_keywords = [
            keyword
            for keyword in SUSPICIOUS_KEYWORDS
            if keyword in url_lower
        ]

        if matched_keywords:
            result["score"] += 10
            result["indicators"].append(
                "Security-related keyword in URL: "
                + ", ".join(matched_keywords)
            )

        # Extract registered domain
        extracted = tldextract.extract(url)

        domain = extracted.domain
        suffix = extracted.suffix

        if domain and suffix:
            result["domain"] = f"{domain}.{suffix}"
        else:
            result["domain"] = hostname

        if len(hostname) > 60:
            result["score"] += 10
            result["indicators"].append(
                "Unusually long hostname"
            )

        result["score"] = min(result["score"], 100)
        result["suspicious"] = result["score"] >= 20

    except Exception as error:
        result["suspicious"] = True
        result["score"] = 30
        result["indicators"].append(
            f"URL analysis error: {error}"
        )

    return result


def analyze_urls(urls: list[str]) -> list[dict]:
    """Analyze multiple URLs."""

    return [analyze_url(url) for url in urls]
