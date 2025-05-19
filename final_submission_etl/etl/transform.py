import pandas as pd

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)

    # Hapus nilai benar-benar invalid
    df = df[~df["title"].isin(["Unknown Product", None])]
    df = df[~df["price"].isin(["Price Unavailable", None])]
    df = df[~df["rating"].isin(["Invalid Rating / 5", "Not Rated", None])]

    # Konversi price ke float dan ke rupiah
    df["price"] = pd.to_numeric(df["price"], errors="coerce") * 16000

    # Ambil angka dari rating
    df["rating"] = df["rating"].astype(str).str.extract(r"([\d.]+)")[0]
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # Ambil angka dari colors, fallback ke "1" jika kosong
    df["colors"] = df["colors"].astype(str).str.extract(r"(\d+)")[0].fillna("1")
    df["colors"] = pd.to_numeric(df["colors"], errors="coerce")

    # Bersihkan label Size dan Gender
    df["size"] = df["size"].astype(str).str.replace("Size:", "", regex=False).str.strip()
    df["gender"] = df["gender"].astype(str).str.replace("Gender:", "", regex=False).str.strip()

    # Drop jika kolom utama masih null
    df.dropna(subset=["price", "rating", "colors", "size", "gender"], inplace=True)

    # df.drop_duplicates(subset=["title"], inplace=True)

    df.reset_index(drop=True, inplace=True)

    # Tipe data sesuai ketentuan reviewer
    df = df.astype({
        "title": "object",
        "price": "float64",
        "rating": "float64",
        "colors": "int64",
        "size": "object",
        "gender": "object"
    })

    return df
