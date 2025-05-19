from etl.extract import extract_data

def test_extract_returns_list():
    data = extract_data()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]
