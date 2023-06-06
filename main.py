import Request.sendXML as req

xmlFile = str(input('put the file name: '))+'.xml'

with open(xmlFile, 'rb') as f:
    files = {'file': f}
    res = req.sendXML(files)

print(res)



