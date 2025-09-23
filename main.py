"""
main.py
-------
Punto de entrada de la POC OCR Transaction Analyzer.

Corre el pipeline completo (OCR → Parser → Scorer) usando
el backend definido (mock o aws).
"""

import argparse
from src import chat_agent, pipeline
from src.utils import ocr_mock


def main():
    print("💬 OCR Transaction Analyzer (Conversational Mode)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("👉 Which comprobante do you want to analyze? ")

        if user_input.lower() in ["exit", "quit", "salir"]:
            print("👋 Exiting...")
            break

        # 1. Ask Claude which file the user meant
        comprobante = chat_agent.get_requested_comprobante(user_input)

        print(f"🤖 Claude selected: {comprobante}")

        # 2. Run pipeline
        try:
            result = pipeline.run_pipeline(f"samples/{comprobante}", backend="mock")
            print("=== Pipeline result ===")
            print(result)
        except FileNotFoundError:
            print(f"❌ File not found: samples/{comprobante}")
        except Exception as e:
            print(f"⚠️ Error running pipeline: {e}")

if __name__ == "__main__":
    main()
