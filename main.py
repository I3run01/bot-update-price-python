import Request.sendXML as req
import json

xmlFile = str(input('put the file name: '))+'.xml'

print(xmlFile)

with open(xmlFile, 'rb') as f:
    files = {'file': f}
    res = req.sendXML(files)

print(res['cnpj'])



