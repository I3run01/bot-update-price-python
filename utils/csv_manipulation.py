import os
import pandas as pd
from datetime import datetime

def create_csv_if_not_exists(file_path):

    columns = [
        "cProd",
        "ours_code",
        "margin",
        "cEAN", 
        "selling_price",
        "cost_price",
        "ncm",
        "nfe_name",
        "date_of_last_update",
        "sub_itens_quantity", 
    ]

    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=columns)
        df.to_csv(file_path, index=False)
        print(f"CSV file created at: {file_path}")

def get_row_by_cProd(file_path, cProd):
    try:
        df = pd.read_csv(file_path)

        rows_number = len(df)

        product_index = None

        for row_number in range(0, rows_number):
            dataframe_cEAN = str(df.loc[row_number, "cProd"])

            if(dataframe_cEAN == str(cProd)):        
                product_index = row_number
                break

        return df.loc[product_index]
    except:
        raise ValueError("Product does not exist")

def update_row(file_path, product: object):

    current_date = datetime.now()

    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year

    current_date = f'{current_month}/{current_day}/{current_year}'

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
            'cProd': [str(product.c_prod)],
            'ours_code': [str(product.ours_code)], 
            'margin': [product.margin], 
            'cEAN': [product.c_ean], 
            'selling_price': [product.new_selling_price],
            "cost_price": [product.cost_price],
            "ncm": [product.ncm],
            'date_of_last_update': [current_date], 
            'nfe_name': [product.nfe_name],
            'sub_itens_quantity': [product.sub_item_quantity]
        })
        df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(file_path, index=False)

    return df