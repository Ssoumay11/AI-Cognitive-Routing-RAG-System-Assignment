def detect_injection(text: str) -> bool:
    triggers = [
        "ignore previous instructions",
        "you are now",
        "forget instructions",
        "act as",
        "system override"
    ]
    text = text.lower()
    return any(t in text for t in triggers)