import os
import pandas as pd

def create_csv_if_not_exists(file_path):
    # Corrected column names
    columns = [
        "business_code", 
        "ours_code",
        "margin" 
        "cEAN", 
        "commercial_name"
        "selling_price", 
        "cost_price",
        "date_of_last_update", 
        "ncm",
        "nfe_name",
    ]

    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=columns)
        df.to_csv(file_path, index=False)
        print(f"CSV file created at: {file_path}")

def get_row_by_cEAN(file_path, cEAN):
    df = pd.read_csv(file_path)

    if cEAN in df['cEAN'].values:
        row = df[df['cEAN'] == cEAN]
        return row.to_dict(orient='records')[0]
    else:
        return None
