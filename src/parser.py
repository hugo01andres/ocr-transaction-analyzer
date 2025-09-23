import re
from typing import Dict

def parse_comprobante_text(text: str) -> Dict:
    """
    Convierte el texto OCR de un comprobante en un diccionario estructurado.
    Usa regex simples como demo (mock).
    """
    data = {}

    # Regex básicos (ajustables según tu comprobante)
    fecha = re.search(r"Fecha:\s*([\d-]+)", text)
    emisor = re.search(r"Emisor:\s*(.+)", text)
    receptor = re.search(r"Receptor:\s*(.+)", text)
    monto = re.search(r"Monto:\s*\$?([\d,]+\.\d{2})", text)
    folio = re.search(r"Folio:\s*(\d+)", text)

    if fecha: data["fecha"] = fecha.group(1).strip()
    if emisor: data["emisor"] = emisor.group(1).strip()
    if receptor: data["receptor"] = receptor.group(1).strip()
    if monto: data["monto"] = float(monto.group(1).replace(",", ""))
    if folio: data["folio"] = folio.group(1).strip()

    return data
