import requests

url = 'https://webhook.site/f94dab35-0b10-4642-93c8-678a4ef81a75'

headers = {
    'Content-type': 'application/json'
}

json = {
    'Teste': 'Testando'
}

session = requests.Session()
session.headers = headers 

response = session.post(url, json=json)

print(response)