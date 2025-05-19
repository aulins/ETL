from etl.extract import extract_data
import json

raw_data = extract_data()

with open("raw_data_clean.json", "w", encoding="utf-8") as f:
    json.dump(raw_data, f, indent=2, ensure_ascii=False)

print(f"Sukses simpan {len(raw_data)} data mentah ke raw_data_clean.json")
