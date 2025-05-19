def save_to_csv(df, filename="products_final.csv"):
    
    df.to_csv(filename, index=False)
