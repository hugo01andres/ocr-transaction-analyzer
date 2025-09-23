"""
Scorer for OCR Transaction Analyzer
-----------------------------------
Responsible for validating and assigning a "score" or decision
to the extracted and parsed receipt.

Basic rules (example):
- Amount > 10,000 → requires manual review.
- Missing or invalid date → automatic rejection.
- If all key fields exist → pre-approved.
"""

from datetime import datetime
from typing import Dict


def validate_date(date_str: str) -> bool:
    """Validates date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except Exception:
        return False


def score_receipt(data: Dict) -> Dict:
    """
    Applies simple business rules to decide if the receipt
    can be auto pre-approved.

    Args:
        data (dict): parsed receipt with fields:
                     date, sender, receiver, amount, reference

    Returns:
        dict: result with status and details
    """
    result = {"status": None, "reason": None, "data": data}

    # Validate required fields
    required = ["date", "sender", "receiver", "amount", "reference"]
    missing = [f for f in required if f not in data or not data[f]]
    if missing:
        result["status"] = "rejected"
        result["reason"] = f"Missing fields: {', '.join(missing)}"
        return result

    # Validate date
    if not validate_date(data["date"]):
        result["status"] = "rejected"
        result["reason"] = "Invalid date"
        return result

    # High amount rule
    if data["amount"] > 10000:
        result["status"] = "manual_review"
        result["reason"] = "High amount requires manual review"
        return result

    # If everything is ok → pre-approved
    result["status"] = "pre_approved"
    result["reason"] = "Meets automatic validation rules"
    return result


if __name__ == "__main__":
    # Quick test with a mock receipt
    sample = {
        "date": "2025-09-20",
        "sender": "Hugo Martinez",
        "receiver": "Andrea Martinez",
        "amount": 1250.00,
        "reference": "123456789",
    }
    scored = score_receipt(sample)
    print(scored)
