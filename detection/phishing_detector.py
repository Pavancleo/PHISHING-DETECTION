import re

phishing_keywords = [
    "verify", "login", "secure", "update",
    "bank", "free", "click", "urgent"
]

def check_url(url):
    score = 0

    if "@" in url:
        score += 1
    if url.count('.') > 3:
        score += 1
    if not url.startswith("https"):
        score += 1

    for word in phishing_keywords:
        if word in url.lower():
            score += 1

    if score >= 3:
        return "⚠️ Phishing URL Detected"
    else:
        return "✅ URL Seems Safe"

url = input("Enter URL to check: ")
print(check_url(url))
