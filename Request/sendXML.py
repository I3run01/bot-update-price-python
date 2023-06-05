import requests

url = 'http://localhost:5000'

def sendXML(files):
    response = requests.post(url, files=files)
    return response.json()





