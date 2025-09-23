# src/utils/generate_transaction_receipt.py

from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

def create_receipt(
    filename: str,
    sender: str = "John Doe",
    receiver: str = "Jane Smith",
    amount: float = 750.0,
    date: str = None,
    out_dir: str = "samples"
):
    """
    Generates a simulated image of a transaction receipt.

    Args:
        filename (str): file name to save (e.g., receipt_750.jpg)
        sender (str): sender's name
        receiver (str): receiver's name
        amount (float): transaction amount
        date (str): date in format dd/mm/yyyy (default: today)
        out_dir (str): folder where receipts are saved
    """
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if date is None:
        date = datetime.today().strftime("%d/%m/%Y")

    # Canvas
    W, H = 800, 400
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # Load font
    try:
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        font = ImageFont.truetype(font_path, 24)
        big = ImageFont.truetype(font_path, 36)
    except:
        font = ImageFont.load_default()
        big = ImageFont.load_default()

    # Header
    draw.text((40, 30), "TRANSACTION RECEIPT", font=font, fill="black")

    # Fields
    draw.text((40, 100), f"Sender: {sender}", font=font, fill="black")
    draw.text((40, 140), f"Receiver: {receiver}", font=font, fill="black")
    draw.text((40, 180), f"Date: {date}", font=font, fill="black")
    draw.text((40, 250), f"Amount: ${amount:.2f} USD", font=big, fill="black")

    # Save
    output_path = os.path.join(out_dir, filename)
    img.save(output_path)
    print(f"[✔] Receipt generated: {output_path}")


if __name__ == "__main__":
    # Generate test receipts
    create_receipt("receipt_120.jpg", amount=120)
    create_receipt("receipt_750.jpg", amount=750)
    create_receipt("receipt_6000.jpg", amount=6000)
