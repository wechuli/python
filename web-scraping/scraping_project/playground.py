from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/page/1/"

response = requests.get(url)

print(response.text)
