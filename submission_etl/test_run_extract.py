from etl.extract import extract_data

data = extract_data()

print(f"Total data hasil extract: {len(data)}")
print("Contoh 3 data teratas:")
for item in data[:3]:
    print(item)
