from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

def crear_comprobante(
    filename: str,
    sender: str = "Juan Pérez",
    receiver: str = "Maria Lopez",
    amount: float = 750.0,
    date: str = None,
    out_dir: str = "samples"
):
    """
    Genera una imagen simulada de un comprobante de pago.

    Args:
        filename (str): nombre del archivo a guardar (ej. comprobante_750.jpg)
        sender (str): nombre del remitente
        receiver (str): nombre del receptor
        amount (float): monto de la transacción
        date (str): fecha en formato dd/mm/yyyy (por defecto hoy)
        out_dir (str): carpeta donde guardar los comprobantes
    """
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if date is None:
        date = datetime.today().strftime("%d/%m/%Y")

    # Crear lienzo
    W, H = 800, 400
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # Intentar cargar fuente
    try:
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        font = ImageFont.truetype(font_path, 24)
        big = ImageFont.truetype(font_path, 36)
    except:
        font = ImageFont.load_default()
        big = ImageFont.load_default()

    # Encabezado
    draw.text((40, 30), "COMPROBANTE DE TRANSFERENCIA", font=font, fill="black")

    # Campos
    draw.text((40, 100), f"Remitente: {sender}", font=font, fill="black")
    draw.text((40, 140), f"Receptor: {receiver}", font=font, fill="black")
    draw.text((40, 180), f"Fecha: {date}", font=font, fill="black")
    draw.text((40, 250), f"Monto: ${amount:.2f} USD", font=big, fill="black")

    # Guardar
    output_path = os.path.join(out_dir, filename)
    img.save(output_path)
    print(f"[✔] Comprobante generado: {output_path}")


if __name__ == "__main__":
    # Generar comprobantes de prueba
    crear_comprobante("comprobante_120.jpg", amount=120)
    crear_comprobante("comprobante_750.jpg", amount=750)
    crear_comprobante("comprobante_6000.jpg", amount=6000)
