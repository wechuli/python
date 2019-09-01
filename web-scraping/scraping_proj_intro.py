# https://www.rithmschool.com/blog?page=5

import requests
from bs4 import BeautifulSoup
from csv import reader, writer
import time
import 


alldata = list()


for page_number in range(1, 10):
    url = f'https://www.rithmschool.com/blog?page={page_number}'
    response_text = requests

    time.sleep(2)
# print(response.text)
time.

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all('article')
print(articles)

with open("blog_data.csv", "w", newline="") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['title', 'link', 'date'])

    for article in articles:
        a_tag = article.find('a')
        # title
        title = a_tag.get_text()
        # href
        url = a_tag['href']
        date = article.find('time')['datetime']
        csv_writer.writerow([title, url, date])
