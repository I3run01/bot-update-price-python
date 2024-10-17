import os
import glob
import utils.csv_manager.csv_manipulation as csv_manipulation
import pandas as pd
from datetime import datetime
import math
from Classes.Product import Product


def show_last_product_update(product_list):
    today = datetime.today().date()

    lower_days_difference = math.inf
    c = 0
    index = None
    for product in product_list:
        if isinstance(product['date_of_last_update'], pd.Series):
            last_update_date = product['date_of_last_update'].iloc[0]
        else:
            last_update_date = product['date_of_last_update']
            c += 1
            continue

        last_update_date = datetime.strptime(last_update_date, '%m/%d/%Y').date()

        days_difference = (today - last_update_date).days

        if days_difference < lower_days_difference:
            index = c

        c += 1

        # print(20*'-')
        # print(product)
        # print(20*'-')

    if index == None:
        print('Product does not exist')
        return

    # print(20*'-=')
    # print(product_list[index])
    # print(20*'-=')

while True:
    product_ours_code = str(input('input the ours code of the product: '))
    directory = 'database'

    print(product_ours_code)

    csv_files = glob.glob(os.path.join(directory, '*.csv'))

    product_datas_list = []
    for csv_path in csv_files:
        csv_path = csv_path.replace('\\', '/')

        try:
            product_datas = csv_manipulation.get_row_by_ours_code(
                csv_path, 
                f'f{product_ours_code}'
            )

            dict = {
                'csv_path': csv_path,
                'dataframe': product_datas
            }
            
            product_datas_list.append(dict)

        except:
            continue
        
    print(4*'-='+ 'Menu' + 4*('-='))
    print('99 - Restart')
    print('1 - Show the last uptade')
    print('2 - Show all products')

    while True:
        option = str(input('option: '))
        confirm = str(input('Confirm (Y/N): ')).strip().upper()

        if confirm not in ['S', 'Y']:
                continue

        if(option == '99'):
            break

        if(option == '1'):
            show_last_product_update(product_list = product_datas_list)

        if(option == '2'):
            for product in product_datas_list:
                print(20*'-=-')
                print('database: ' + product['csv_path'])
                print(product['dataframe'])
                print(20*'-=-')
        



