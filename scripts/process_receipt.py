import pytesseract
from PIL import Image
import os
import csv
from datetime import datetime
import shutil

receipts_folder = "receipts"
processed_folder = "processed"
csv_file = "data/expenses.csv"

# recorrer facturas
for file in os.listdir(receipts_folder):

    if file.endswith(".jpg") or file.endswith(".png"):

        path = os.path.join(receipts_folder, file)

        image = Image.open(path)

        # leer texto de la factura
        text = pytesseract.image_to_string(image)

        with open(csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow([
                file,
                text.replace("\n"," "),
                datetime.now()
            ])

        shutil.move(path, os.path.join(processed_folder, file))

print("Receipts processed successfully")
