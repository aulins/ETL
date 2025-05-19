from etl.load import save_to_csv
import pandas as pd
import os

def test_save_to_csv_creates_file():
    df = pd.DataFrame([{
        "title": "Test Product",
        "price": 1600000.0,
        "rating": 3.9,
        "colors": 3,
        "size": "M",
        "gender": "Women"
    }])
    save_to_csv(df, "test_output.csv")
    assert os.path.exists("test_output.csv")
    os.remove("test_output.csv")
