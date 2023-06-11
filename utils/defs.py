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
    else:
        print(f"CSV file already exists at: {file_path}")
