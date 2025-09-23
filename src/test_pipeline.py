from utils.ocr_mock import extract_text_from_comprobante
from parser import parse_comprobante_text

if __name__ == "__main__":
    text = extract_text_from_comprobante("samples/comprobante_120.jpg")
    parsed = parse_comprobante_text(text)
    print(parsed)