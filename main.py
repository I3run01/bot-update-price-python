import Request.sendXML as req
import utils.csv_manipulation as csv_manipulation
from Classes.Product import Product
from termcolor import colored
from colored import fg, attr
from utils.obj_from_list import find_product_by_ean
import utils.londrisoft_bot as bot
import time

def show_products_list():
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
        print(f'Price (R$): {colored(item.old_selling_price, "red")} -> {colored(item.new_selling_price, "green")}')
        print('')
        print(30*'=')

products_list = []

while True:
    try:
        xmlFile = str(input('put the file name: '))+'.xml'

        with open(xmlFile, 'rb') as f:
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
        product_datas = csv_manipulation.get_row_by_cProd(csv_path, product['cProd'])

        new_product = Product(
                c_prod = f'#{product["cProd"]}',
                ours_code = product_datas["ours_code"],
                c_ean = product_datas['cEAN'],
                cost_price= float(product['costPrice']),
                ncm = product['ncm'],
                cest = product['cest'],
                commercial_name = product['comercialName'],
                nfe_name= product['nfeName'],
                margin=product_datas["margin"],
                old_selling_price = product_datas["selling_price"],
            )
        
        if(product_datas["sub_itens_quantity"]):
            product_datas_sub_itens_quantity = product_datas["sub_itens_quantity"]

            new_product.sub_item_quantity = float(product_datas_sub_itens_quantity)

        products_list.append(new_product)
        
    except:
        new_product = Product(
                c_prod = f'#{product["cProd"]}',
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

        products_list.append(new_product)

show_products_list()

while True:

    print(30*'=')

    try:
        print('0 - Change the product margin.')
        print('1 - Insert the quantity for the sub-item.')
        print('2 - Change the cEAN of the products.')
        print('3 - Create, print and update the products that increased')
        print('4 - Just Create and update the products that increased')
        print('5 - Just print the products that increased')
        print('9 - Show all products ')
        print(30*'=')

        print('')

        option = str(input('option: '))
        confirm = str(input('Confirm: ').upper()[0])

        if(confirm != 'S'):
            continue

        if(option == '0'):
            print(30*'=')

            print('You selected the option 0')
            time.sleep(0.5)

            product_cEAN = str(input(f'To change the margin, first put the product {colored("cEAN", "yellow")}: '))

            product = find_product_by_ean(products_list, product_cEAN)

            if product is None:
                raise ValueError("Product not found")
            
            try:
                new_margin = float(input('put the product margin, *NOT decimal*: '))
            except:
                raise ValueError("Margin should be a number")
            
            product.margin = new_margin

            print(f'the new margin of the {product.commercial_name} is {product.margin}')

            time.sleep(1)

            show_products_list()

            print(30*'=')

        elif(option == '1'):
            print('You selected the option 1')
            time.sleep(1)

            for product in products_list:
                
                if(product.ours_code != None):
                    continue

                print(f'the product name is: {colored(product.nfe_name, "blue")}')

                sub_item_quantity = float(input('Put the quantity of the sub-item: '))

                product.sub_item_quantity = sub_item_quantity

                time.sleep(.5)

                print(f'the new price of the product is {colored(product.new_selling_price, "green")}')

                time.sleep(1)

                print(30 * '-')

        elif(option == '2'):
            print('op 2: You will change the cEAN')
            time.sleep(1)

            for product in products_list:
                
                if(product.ours_code != None):
                    continue

                print(f'the product name is: {colored(product.nfe_name, "blue")}')

                new_c_ean = float(input('Put the new cEAN: '))

                product.c_ean = new_c_ean

                time.sleep(.5)

                print(f'the new CEAN is {colored(product.c_ean, "yellow")}')

                time.sleep(1)

                print(30 * '-')

        elif(option == '3'):
            print('You selected the option 2')
            time.sleep(1)
            bot.update_and_print_products(products_list, 'increase')

            for product in products_list:
                if(float(product.new_selling_price) > float(product.old_selling_price)):
                    csv_manipulation.update_row(csv_path, product)

        elif(option == '4'):
            print('You selected the option 3')
            time.sleep(1)

            bot.just_update_products(products_list, 'increase')

            for product in products_list:
               if(float(product.new_selling_price) > float(product.old_selling_price)):
                    csv_manipulation.update_row(csv_path, product)
      
        elif(option == '5'):
            print('You selected the option 4')
            time.sleep(1)

            bot.just_print_products(products_list, 'increase')

            for product in products_list:
                if(float(product.new_selling_price) > float(product.old_selling_price)):
                    csv_manipulation.update_row(csv_path, product)

        elif(option == '9'):
            show_products_list()

        elif(option == '3'):
            print('You selected the option 2')
            time.sleep(1)
            bot.update_and_print_products(products_list, 'increase')

            for product in products_list:
                if(float(product.new_selling_price) > float(product.old_selling_price)):
                    csv_manipulation.update_row(csv_path, product)

        elif(option == '4'):
            print('You selected the option 3')
            time.sleep(1)

            bot.just_update_products(products_list, 'increase')

            for product in products_list:
               if(float(product.new_selling_price) > float(product.old_selling_price)):
                    csv_manipulation.update_row(csv_path, product)
      
        elif(option == '5'):
            print('You selected the option 4')
            time.sleep(1)

            bot.just_print_products(products_list, 'increase')

            for product in products_list:
                if(float(product.new_selling_price) > float(product.old_selling_price)):
                    csv_manipulation.update_row(csv_path, product)

        elif(option == '9'):
            show_products_list()

    except Exception as e:
        print(colored(f"Caught an error: {e}", 'red'))
        time.sleep(2)
        continue