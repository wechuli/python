from bs4 import BeautifulSoup
import requests


# # - After every incorrect guess, the player receives a hint about the author.
#   - For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.
#   - The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.

base_url = "http://quotes.toscrape.com"

author_details_raw = requests.get(
    'http://quotes.toscrape.com/author/Albert-Einstein/').text

soup = BeautifulSoup(author_details_raw, 'html.parser')

author_dob = soup.select('.author-born-date')[0].get_text()
author_birth_location = soup.select('.author-born-location')[0].get_text()
author_first_name = soup.select('.author-title')[0].get_text().split(' ')[0]
author_last_name = soup.select('.author-title')[0].get_text().split(' ')[1]

print(author_dob, author_birth_location, author_first_name, author_last_name)
