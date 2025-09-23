# src/utils/ocr_mock.py

def extract_text_from_comprobante(file_path: str) -> str:
    """
    Mock de OCR para comprobantes.
    Devuelve texto simulado como si fuera el resultado de AWS Textract.
    """
    return """
    Banco Ejemplo S.A.
    Fecha: 2025-09-20
    Emisor: Hugo Martinez
    Receptor: Andrea Martinez
    Monto: $1,250.00 MXN
    Folio: 123456789
    """