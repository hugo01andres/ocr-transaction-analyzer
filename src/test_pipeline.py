from utils.ocr_mock import extract_text_from_receipt
from parser import parse_receipt_text

if __name__ == "__main__":
    text = extract_text_from_receipt("samples/comprobante_120.jpg")
    parsed = parse_receipt_text(text)
    print(parsed)