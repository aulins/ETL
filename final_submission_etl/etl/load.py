def save_to_csv(df, filename="products.csv"):
    
    df.to_csv(filename, index=False)
