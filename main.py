"""
main.py
-------
Punto de entrada de la POC OCR Transaction Analyzer.

Corre el pipeline completo (OCR → Parser → Scorer) usando
el backend definido (mock o aws).
"""

import argparse
from .src import pipeline

def main():
    parser = argparse.ArgumentParser(description="OCR Transaction Analyzer POC")
    parser.add_argument(
        "--file", type=str, default="samples/comprobante_120.jpg",
        help="Ruta al comprobante a procesar"
    )
    parser.add_argument(
        "--backend", type=str, choices=["mock", "aws"], default="mock",
        help="Backend OCR: mock (simulado) o aws (Textract)"
    )
    args = parser.parse_args()

    result = pipeline.run_pipeline(args.file, backend=args.backend)
    print("=== Resultado del pipeline ===")
    print(result)

if __name__ == "__main__":
    main()
