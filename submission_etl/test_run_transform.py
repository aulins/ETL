from etl.extract import extract_data
from etl.transform import transform_data

def main():
    raw = extract_data()
    print(f"\nJumlah data hasil extract: {len(raw)}")

    df = transform_data(raw)
    print(f"Jumlah data hasil transform: {len(df)}")

    print("\n📋 5 Data Teratas:")
    print(df.head())

    print("\n🧠 Struktur Kolom dan Tipe Data:")
    print(df.dtypes)

    print("\n🧼 Jumlah NULL per Kolom:")
    print(df.isnull().sum())

    print("\n🔁 Jumlah Baris Duplikat:")
    print(df.duplicated().sum())

    print("\n🔍 Contoh Nilai Unik Kolom:")
    print("Size:", df['size'].unique())
    print("Gender:", df['gender'].unique())
    print("Colors:", df['colors'].unique())

if __name__ == "__main__":
    main()
