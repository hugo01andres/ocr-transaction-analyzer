from utils import ocr_mock  # temporal
# from utils import ocr_extractor  # real cuando actives AWS

def read_text(file_path: str, backend: str = "mock") -> str:
    if backend == "mock":
        return ocr_mock.extract_text_from_comprobante(file_path)
    elif backend == "aws":
        # Aquí iría la llamada real a ocr_extractor con Textract
        # TODO: integrar AWS Textract cuando la cuenta esté activa
        raise NotImplementedError("AWS Textract aún no está habilitado.")
    else:
        raise ValueError("Backend no soportado.")
    
if __name__ == "__main__":
    text = read_text("samples/comprobante_120.jpg", backend="mock")
    print(text)
