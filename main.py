import Request.sendXML as req
import utils.csv_manipulation as csv_manipulation
from Classes.Product import Product
from termcolor import colored

products_list = []

xmlFile = str(input('put the file name: '))+'.xml'

with open(xmlFile, 'rb') as f:
    files = {'file': f}
    res = req.sendXML(files)

csv_path = f'database/{res["name"]}.csv'

products = res['products']

csv_manipulation.create_csv_if_not_exists(csv_path)

for product in products:
    datas = csv_manipulation.get_row_by_cEAN(csv_path, product['cEAN'])

    if(datas == None):
        new_product = Product(
            is_new = True,
            ours_code = None,
            c_ean = product['cEAN'],
            cost_price= float(product['costPrice']),
            ncm = product['ncm'],
            commercial_name = product['comercialName'],
            nfe_name= product['nfeName'],
            margin=50,
            old_selling_price = 0
        )

        products_list.append(new_product)

c = 0
for item in products_list:
    print(30*'=')
    print('')
    print(f'comercial name: {item.commercial_name}')
    print(f'our code: {item.ours_code}')
    print(f'NFE name: {item.nfe_name}')
    print(f'cEAN: {colored(item.c_ean, "yellow")}')
    print(f'Margin: {item.margin}')
    print(f'Price: {colored(item.old_selling_price, "red")} -> {colored(item.selling_cost, "green")}')
    print('')
    print(30*'=')
    c = c+1


