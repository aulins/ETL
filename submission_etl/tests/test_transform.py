from etl.transform import transform_data

def test_transform_returns_dataframe():
    raw = [
        {
            "title": "Hoodie 3",
            "price": "496.88",
            "rating": "Rating: ⭐ 4.8 / 5",
            "colors": "3 Colors",
            "size": "XL",
            "gender": "Gender: Unisex"
        }
    ]
    df = transform_data(raw)
    assert df.shape[0] == 1
    assert "price" in df.columns
    assert df["price"].iloc[0] == 496.88 * 16000
