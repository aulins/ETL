from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import save_to_csv

def main():
    raw = extract_data()
    clean = transform_data(raw)
    save_to_csv(clean)

if __name__ == "__main__":
    main()
