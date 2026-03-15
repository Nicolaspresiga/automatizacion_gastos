import pytesseract
from PIL import Image
import os
import csv
from datetime import datetime
import shutil

receipts_folder = "receipts"
processed_folder = "processed"
csv_file = "data/expenses.csv"

for file in os.listdir(receipts_folder):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        try:
            path = os.path.join(receipts_folder, file)

            # abrir imagen
            image = Image.open(path)

            # convertir formato seguro
            image = image.convert("RGB")

            text = pytesseract.image_to_string(image)

            with open(csv_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    file,
                    text.replace("\n"," "),
                    datetime.now()
                ])

            shutil.move(path, os.path.join(processed_folder, file))

        except Exception as e:
            print(f"Error processing {file}: {e}")

print("Receipts processed successfully")

