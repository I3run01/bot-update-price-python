import requests

url = 'https://apinfe-priceupdate.onrender.com'
# url = 'http://127.0.0.1:5000'

def sendXML(files):
    response = requests.post(url, files=files)
    return response.json()
