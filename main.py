import Request.sendXML as req

xmlFile = str(input('put the file name: '))+'.xml'

with open(xmlFile, 'rb') as f:
    files = {'file': f}
    res = req.sendXML(files)

c=0
for products in res['products']:
    print(c)
    print(f"cProd: {products['cProd']}")
    print(f"cEAN: {products['cEAN']}")
    print(f"nfeName: {products['nfeName']}")
    print(f"ncm: {products['ncm']}")
    print(f"costPrice: {products['costPrice']}")
    print(f"comercialName: {products['comercialName']}")
    print('')

    c = c+1




