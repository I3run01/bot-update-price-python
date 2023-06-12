import requests

url = 'https://apinfe-priceupdate.onrender.com'

def sendXML(files):
    response = requests.post(url, files=files)
    return response.json()
