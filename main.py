import Request.sendXML as req
import utils.csv_manipulation as csv_manipulation
import Classes.Product as Product

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
            is_new=True,
            ours_code='ABC123',
            c_ean='1234567890123',
            cost_price=10.5,
            ncm='1234.56.78',
            commercial_name='Cool Gadget',
            margin=0.2,
            old_selling_price=9.0
        )

        print(new_product.commercial_name)  # prints: Cool Gadget
        print(new_product.cost_price)  # prints: 10.5
        print(new_product.selling_cost)
