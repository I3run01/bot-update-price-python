import Request.sendXML as req
import utils.csv_manipulation as csv_manipulation
from Classes.Product import Product
from termcolor import colored
from colored import fg, attr
import utils.bot.londrisoft_bot as bot
from tkinter import filedialog
import tkinter as tk
import time

def nfe_product():
    products_list = []

    def show_products_list():
        all_products_have_code = True
        None_of_the_products_had_price_increased = True

        for item in products_list:

            margin_color = 'blue' if float(item.margin) != 50 else 'white'
            ours_code_color = 'cyan' if item.ours_code != None else 'white'

            print(30*'=')
            print('')
            print(f'comercial name: {item.commercial_name}')
            print(f'our code: {fg(ours_code_color)}{item.ours_code}{attr(0)}')
            print(f'NFE name: {item.nfe_name}')
            print(f'cEAN: {colored(item.c_ean, "yellow")}')
            print(f'Margin (%): {fg(margin_color)}{item.margin}{attr(0)}')

            min_price_formatted = f"{item.min_new_selling_price:.2f}"
            print(f'min price (R$): {colored(min_price_formatted, "yellow")}')

            print(f'Price (R$): {colored(item.old_selling_price, "red")} -> {colored(item.new_selling_price, "green")}')

            max_price_formatted = f"{item.max_new_selling_price:.2f}"
            print(f'max price (R$): {colored(max_price_formatted, "magenta")}')

            print('')
            
            if(item.ours_code == None and item.c_ean == None):
                print(f'this product has no {colored("cEAN", "red")} and no {colored("Ours_code", "red")}')
                print('')

            print(30*'=')

            if(item.ours_code == None):
                all_products_have_code = False
            
            if(item.new_selling_price > item.old_selling_price):
                None_of_the_products_had_price_increased = False

        if(all_products_have_code and None_of_the_products_had_price_increased):
            text = "None of the products needs to be updated".upper()
            print(f'{colored(text, "green")}')

    def all_products_have_ours_code_or_cEAN():

        have = True
        for product in products_list:
            if(have == False):
                return False
            
            if(product.ours_code or product.c_ean):
                continue

            have = False

        return have

    while True:
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])

            with open(file_path, 'rb') as f:
                files = {'file': f}
                res = req.sendXML(files)

            break

        except:
            continue

    csv_path = f'database/{res["name"]}.csv'

    products = res['products']

    csv_manipulation.create_csv_if_not_exists(csv_path)

    for product in products:
        try:
            product_datas = csv_manipulation.get_row_by_cProd(
                csv_path, 
                f'f{product["cProd"]}'
            )
        
            new_product = Product(
                    c_prod = f'f{product["cProd"]}',
                    ours_code = product_datas["ours_code"][1:],
                    c_ean = product_datas['cEAN'][1:],
                    cost_price= float(product['costPrice']),
                    ncm = product['ncm'],
                    cest = product['cest'],
                    commercial_name = product['comercialName'],
                    nfe_name= product['nfeName'],
                    margin=product_datas["margin"],
                    old_selling_price = float(product_datas["selling_price"]),
                )
            
            if(str(product_datas["sub_itens_quantity"]) != 'nan'):
                product_datas_sub_itens_quantity = product_datas["sub_itens_quantity"]
                new_product.sub_item_quantity = float(product_datas_sub_itens_quantity)

            products_list.append(new_product)
            
        except:
            new_product = Product(
                    c_prod = f'f{product["cProd"]}',
                    ours_code = None,
                    c_ean = product['cEAN'],
                    cost_price= float(product['costPrice']),
                    ncm = product['ncm'],
                    cest = product['cest'],
                    commercial_name = product['comercialName'],
                    nfe_name= product['nfeName'],
                    margin=50,
                    old_selling_price = 0,
                )
            
            if(
                new_product.c_ean[0] == '0' and
                new_product.c_ean[1] == '0' and
                new_product.c_ean[2] == '0' and
                new_product.c_ean[3] == '0' 
            ):
                new_product.c_ean = str(int(new_product.c_ean))
    
            products_list.append(new_product)

    show_products_list()

    while True: 

        print(30*'=')

        try:
            print('0 - Change the product margin.')
            print('1 - Insert the quantity for the sub-item.')
            print('2 - Change the cEAN of the products.')
            print('3 - Create, print and update the products')
            print('8 - To put ours_code')
            print('9 - Show all products')
            print('99 - return')
            print(30*'=')

            print('')

            option = str(input('option: '))
            confirm = str(input('Confirm: ').upper()[0])

            if(confirm != 'S'):
                continue

            if(option == '0'):
                print('OP 0: Change producs margin')
                time.sleep(1)

                for product in products_list:
                    
                    if(product.ours_code != None):
                        continue

                    print(f'the product name is: {colored(product.nfe_name, "blue")}')

                    new_margin = str(input('Put the new margin or Just press enter to ignore: '))

                    if(new_margin == ''):
                        continue

                    product.margin = float(new_margin)

                    time.sleep(.5)

                    print(f'the new Margin {colored(product.margin, "yellow")}')

                    time.sleep(1)

                    print(30 * '-')

            elif(option == '1'):
                print('OP: 1. Insert the quantity for the sub-item.')
                time.sleep(1)

                for product in products_list:
                    
                    if(product.ours_code != None):
                        continue

                    print(f'the product name is: {colored(product.nfe_name, "blue")}')
                    
                    sub_item_quantity = input('Put the quantity of the sub-item or Press Enter to ignore: ')

                    if(sub_item_quantity == ''):
                        continue

                    product.sub_item_quantity = float(sub_item_quantity)

                    time.sleep(.5)

                    print(f'the new price of the product is {colored(product.new_selling_price, "green")}')

                    time.sleep(1)

                    print(30 * '-')

            elif(option == '2'):
                print('OP 2: You will change the cEAN')
                time.sleep(1)

                for product in products_list:
                    
                    if(product.ours_code != None):
                        continue

                    print(f'the product name is: {colored(product.nfe_name, "blue")}')

                    new_c_ean = str(input('Put the new cEAN or press enter to ignore: '))

                    if(new_c_ean == ''):
                        continue

                    product.c_ean = new_c_ean

                    time.sleep(.5)

                    print(f'the new CEAN is {colored(product.c_ean, "yellow")}')

                    time.sleep(1)

                    print(30 * '-')

            elif(option == '3'):
                print('OP: 3. Create, print and update the products that increased')

                time.sleep(1)

                if(all_products_have_ours_code_or_cEAN() != True):
                    raise ValueError("All Products should cEAN or Ours code")

                bot.update_and_print_products(products_list)

                for product in products_list:
                    if(float(product.new_selling_price) > float(product.old_selling_price)):
                        csv_manipulation.update_row(csv_path, product)

            elif(option == '8'):
                print('OP 8: Change ours code')
                time.sleep(1)

                for product in products_list:
                    
                    if(product.ours_code != None):
                        continue

                    print(f'the product name is: {colored(product.nfe_name, "blue")}')

                    new_ours_code = str(input('Put the new Ours code or JUST press enter to ignore: '))

                    if(new_ours_code == ''):
                        continue

                    product.ours_code = new_ours_code

                    time.sleep(.5)

                    print(f'the new Ours_code is {colored(product.ours_code, "yellow")}')

                    time.sleep(1)

                    print(30 * '-')

            elif(option == '9'):
                show_products_list()

        except Exception as e:
            print(colored(f"Caught an error: {e}", 'red'))
            time.sleep(2)
            continue

        if(option == '99'):
            return

while True: 
    time.sleep(0.5)     
    nfe_product()