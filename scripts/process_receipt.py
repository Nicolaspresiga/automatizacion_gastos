import pytesseract
from PIL import Image
import os
import csv
from datetime import datetime
import shutil
import re

receipts_folder = "receipts"
processed_folder = "processed"
csv_file = "data/expenses.csv"

def extract_total(text):
    # buscar números que parecen montos
    matches = re.findall(r"\d+\.\d{2}", text)

    if matches:
        return max(matches, key=float)

    return "Not detected"


for file in os.listdir(receipts_folder):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        try:
            path = os.path.join(receipts_folder, file)

            image = Image.open(path)
            image = image.convert("RGB")

            text = pytesseract.image_to_string(image)

            total = extract_total(text)

            with open(csv_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)

                writer.writerow([
                    file,
                    total,
                    datetime.now(),
                    text.replace("\n", " ")
                ])

            shutil.move(path, os.path.join(processed_folder, file))

        except Exception as e:
            print(f"Error processing {file}: {e}")

print("Receipts processed successfully")

