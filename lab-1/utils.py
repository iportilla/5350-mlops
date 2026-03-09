import string
from typing import Dict


def extract_features(email_text: str) -> Dict[str, int]:
    """Extract simple numeric features from raw email text."""
    length = len(email_text)
    punct = sum(1 for ch in email_text if ch in string.punctuation)

    return {
        "length": length,
        "punct": punct,
    }
