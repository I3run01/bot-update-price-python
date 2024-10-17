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
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    matching_rows = df[df['cProd'] == cProd]

    if not matching_rows.empty:
        return matching_rows.iloc[-1]
    else:
        # If no match is found, raise an error or return a message
        return "Product does not exist"

def get_row_by_ours_code(file_path, cProd):
    try:
        df = pd.read_csv(file_path, index_col="ours_code")
        return df.loc[str(cProd)]
    except KeyError:
        raise ValueError("Product does not exist")
    
def update_row(file_path, product):
    current_date = datetime.now().strftime('%m/%d/%Y')
    df = pd.read_csv(file_path, index_col="cProd")
    
    product_cProd = str(product.c_prod)
    
    if product_cProd in df.index:
        df.at[product_cProd, 'selling_price'] = product.new_selling_price
        df.at[product_cProd, 'cost_price'] = product.cost_price
        df.at[product_cProd, 'date_of_last_update'] = current_date
    else:
        new_row = pd.DataFrame({
            'cProd': [product_cProd],
            'ours_code': [f'f{product.ours_code}'],
            'margin': [product.margin],
            'cEAN': [f'{product.c_ean}'],
            'selling_price': [product.new_selling_price],
            "cost_price": [product.cost_price],
            "ncm": [product.ncm],
            'date_of_last_update': [current_date],
            'nfe_name': [product.nfe_name],
            'sub_itens_quantity': [product.sub_item_quantity]
        }).set_index('cProd')

        new_row = new_row.dropna(axis=1, how='all')
        df = pd.concat([df, new_row])
    
    df.to_csv(file_path)

    return df
