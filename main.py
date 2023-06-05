import Request.sendXML as req

with open('example.xml', 'r') as xml_file:
    xml_data = xml_file.read()

req = req.sendXML(xml_data)
print(req)

