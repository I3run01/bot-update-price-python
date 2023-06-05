import requests

url = 'http://localhost:5000'
def sendXML(xml_data):
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(url, data=xml_data, headers=headers)
    return response.json()





