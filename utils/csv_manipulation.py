import os
import pandas as pd
from datetime import datetime

def create_csv_if_not_exists(file_path):
    # Corrected column names
    columns = [
        "ours_code",
        "margin",  # added comma here
        "cEAN", 
        "selling_price", 
        "date_of_last_update", 
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

def update_row(file_path, product: object):

    current_date = datetime.now()

    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year

    current_date = f'{current_month}/{current_day}/{current_year}'

    # TODO: read this article: https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/

    df = pd.read_csv(file_path)

    rows_number = len(df)

    product_index = None

    for row_number in range(0, rows_number):
        dataframe_ours_code = str(df.loc[row_number, "ours_code"])
        product_ours_code = str(product.ours_code)

        if(dataframe_ours_code == product_ours_code):        
            product_index = row_number
            break
    
    if(product_index != None):
        df.loc[product_index, 'selling_price'] = product.new_selling_price
        df.loc[product_index, 'date_of_last_update'] = current_date

    else:
        new_row = pd.DataFrame({
            'ours_code': [product.ours_code], 
            'margin': [product.margin], 
            'cEAN': [product.c_ean], 
            'selling_price': [product.new_selling_price], 
            'date_of_last_update': [current_date], 
            'nfe_name': [product.nfe_name]
        })
        df = pd.concat([df, new_row], ignore_index=True)

        df.to_csv(file_path, index=False)

    return df