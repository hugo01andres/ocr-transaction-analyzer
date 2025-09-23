import re
from typing import Dict

import re
from typing import Dict

def parse_receipt_text(text: str) -> Dict:
    """
    Converts the OCR text of a receipt into a structured dictionary.
    Uses simple regex as a demo (mock).
    """
    data = {}

    # Regex for fields
    date = re.search(r"Date:\s*(\d{4}-\d{2}-\d{2})", text)
    sender = re.search(r"Sender:\s*(.+)", text)
    receiver = re.search(r"Receiver:\s*(.+)", text)
    amount = re.search(r"Amount:\s*\$?([\d,]+\.\d{2})", text)
    reference = re.search(r"(?:Reference|Transaction ID):\s*([A-Za-z0-9-]+)", text)

    if date: data["date"] = date.group(1).strip()
    if sender: data["sender"] = sender.group(1).strip()
    if receiver: data["receiver"] = receiver.group(1).strip()
    if amount: data["amount"] = float(amount.group(1).replace(",", ""))
    if reference: data["reference"] = reference.group(1).strip()

    return data
