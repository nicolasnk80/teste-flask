import requests

url = 'http://localhost:5000/data'
params = {'name': 'João'}

response = requests.get(url, params=params)
response.encoding = 'utf-8'  # Definindo a codificação para UTF-8

print(response.json())
