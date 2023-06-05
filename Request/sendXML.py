import requests

url = 'http://example.com/api'
def sendXML(xml_data):
    headers = {'Content-Type': 'application/xml'}
    return requests.post(url, data=xml_data, headers=headers)





