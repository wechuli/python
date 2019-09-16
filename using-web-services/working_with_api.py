import requests
url = 'https://icanhazdadjoke.com/'

# response = requests.get(url, headers={'Accept': 'text/plain'})

response = requests.get(url, headers={'Accept': 'application/json'})
data = response.json()

# print(type(response.text))

print(type(response.text))
print(type(response.json()))

print(data)

print(data['id'])
