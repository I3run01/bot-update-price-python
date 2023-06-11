import Request.sendXML as req
import utils.defs as defs

xmlFile = str(input('put the file name: '))+'.xml'

with open(xmlFile, 'rb') as f:
    files = {'file': f}
    res = req.sendXML(files)

csv_path = f'database/{res["name"]}.csv'

defs.create_csv_if_not_exists(csv_path)
