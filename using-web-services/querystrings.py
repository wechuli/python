# A query string is a way to pass data to the server as part of a GET request
import requests
import pprint
import json


base_url = 'https://icanhazdadjoke.com/search'

# we can pass query strings as params

# response = requests.get(url, headers={'Accept': 'text/plain'})

response = requests.get(
    base_url, headers={'Accept': 'application/json'}, params={"term": "dadaasss", "limit": 20})
data = response.json()

print(data['results'])

pprint.pprint(json.loads(json.dumps(data)))
