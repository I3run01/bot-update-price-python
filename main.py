import Request.sendXML as req

xmlFile = str(input('put the file name: '))+'.xml'

print(xmlFile)

with open(xmlFile, 'r') as xml_file:
    xml_data = xml_file.read()

res = req.sendXML(xml_data)
print(res)

