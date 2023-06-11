import requests

#url = 'http://localhost:5000'
url = 'https://apinfe-priceupdate.onrender.com'

def sendXML(files):
    response = requests.post(url, files=files)
    return response.json()





