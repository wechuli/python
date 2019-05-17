import requests


muyrequest = requests.get(
    "https://www.microsoftedgeinsider.com/en-us/welcome/update?channel=dev&version=76.0.159.0")

print(muyrequest)
print(muyrequest.text)
