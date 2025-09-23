"""
Pipeline principal de la POC OCR Transaction Analyzer
-----------------------------------------------------
Flujo:
1. OCR (mock o AWS Textract) para extraer texto.
2. Parser convierte el texto en JSON estructurado.
3. Scorer valida los datos y da pre-aprobación.
"""

from .utils import ocr_mock
# from utils.ocr_extractor import upload_to_s3, extract_text_from_s3  # TODO: habilitar cuando Textract esté listo
from .parser import parse_receipt_text
from .scorer import score_receipt


def run_pipeline(file_path: str, backend: str = "mock"):
    """
    Ejecuta el pipeline de OCR -> Parser -> Scorer.

    Args:
        file_path (str): ruta del comprobante (jpg/pdf).
        backend (str): 'mock' o 'aws'. Default: 'mock'.

    Returns:
        dict: comprobante procesado con resultado de validación.
    """
    # 1. OCR
    if backend == "mock":
        text = ocr_mock.extract_text_from_receipt(file_path)
    elif backend == "aws":
        # TODO: usar Textract cuando la cuenta AWS esté activa
        raise NotImplementedError("TODO integration with AWS tEXTRACT.")
    else:
        raise ValueError("Backend not available. Use 'mock' or 'aws'.")

    # 2. Parser
    parsed = parse_receipt_text(text)

    # 3. Scorer
    scored = score_receipt(parsed)

    return scored


if __name__ == "__main__":
    result = run_pipeline("samples/transaction_receipt_120.jpg", backend="mock")
    print("Resultado final del pipeline:")
    print(result)
