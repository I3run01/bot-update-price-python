import Request.sendXML as req
import utils.csv_manipulation as csv_manipulation

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
        print('no datas received')
        print("")
