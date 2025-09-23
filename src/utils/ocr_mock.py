# src/utils/ocr_mock.py

def extract_text_from_receipt(file_path: str) -> str:
    """
    Mock OCR for transaction receipts.
    Returns simulated text as if it came from AWS Textract.
    The response varies depending on the receipt number in the filename.
    """
    # Map of sample receipts
    mock_receipts = {
        "transaction_receipt_120.jpg": """
        Example Bank Inc.
        Date: 2025-09-20
        Sender: Hugo Martinez
        Receiver: Andrea Martinez
        Amount: $250.00 MXN
        Transaction ID: 123456789
        """,
        "transaction_receipt_6000.jpg": """
        Global Payments Ltd.
        Date: 2025-09-18
        Sender: John Smith
        Receiver: Jane Doe
        Amount: $9,999.99 USD
        Transaction ID: 60001234
        """,
        "transaction_receipt_750.jpg": """
        FutureBank
        Date: 2025-09-15
        Sender: Alice Johnson
        Receiver: Bob Williams
        Amount: $25,000.00 MXN
        Transaction ID: 75098765
        """
    }

    file_name = file_path.split("/")[-1]  # Extract just the file name
    return mock_receipts.get(file_name, """
        Unknown Bank
        Date: 2025-09-01
        Sender: Test User
        Receiver: Unknown
        Amount: $0.00 USD
        Transaction ID: N/A
    """)
