"""
Scorer del pipeline OCR Transaction Analyzer
--------------------------------------------
Se encarga de validar y asignar un "score" o decisión
al comprobante extraído y parseado.

Reglas básicas (ejemplo):
- Monto > 10,000 → requiere revisión manual.
- Fecha faltante o inválida → rechazo automático.
- Si todos los campos clave existen → pre-aprobado.
"""

from datetime import datetime
from typing import Dict


def validate_date(date_str: str) -> bool:
    """Valida formato de fecha (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except Exception:
        return False


def score_comprobante(data: Dict) -> Dict:
    """
    Aplica reglas de negocio simples para decidir si el comprobante
    se puede pre-aprobar automáticamente.

    Args:
        data (dict): comprobante parseado con campos:
                     fecha, emisor, receptor, monto, folio

    Returns:
        dict: resultado con status y detalles
    """
    result = {"status": None, "reason": None, "data": data}

    # Validar campos obligatorios
    required = ["fecha", "emisor", "receptor", "monto", "folio"]
    missing = [f for f in required if f not in data or not data[f]]
    if missing:
        result["status"] = "rejected"
        result["reason"] = f"Campos faltantes: {', '.join(missing)}"
        return result

    # Validar fecha
    if not validate_date(data["fecha"]):
        result["status"] = "rejected"
        result["reason"] = "Fecha inválida"
        return result

    # Regla de monto alto
    if data["monto"] > 10000:
        result["status"] = "manual_review"
        result["reason"] = "Monto alto requiere revisión manual"
        return result

    # Si todo bien → pre-aprobado
    result["status"] = "pre_approved"
    result["reason"] = "Cumple con validaciones automáticas"
    return result


if __name__ == "__main__":
    # Prueba rápida con un mock
    sample = {
        "fecha": "2025-09-20",
        "emisor": "Hugo Martinez",
        "receptor": "Andrea Martinez",
        "monto": 1250.00,
        "folio": "123456789",
    }
    scored = score_comprobante(sample)
    print(scored)
