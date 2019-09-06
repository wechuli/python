from bs4 import BeautifulSoup
import time
import requests
import random


# the base url

base_url = "http://quotes.toscrape.com"

# get all the html for the quotes

page = 1
allquotes = ""
while(True):
    response = requests.get(f'{base_url}/page/{page}').text
    allquotes = allquotes + response
    print(f'{page * (".")}')
    page += 1

    if (response.find('<li class="next">') == -1):
        break

# use beautiful soup to loop through each quote and create a list of dictionary, each dictionary being a quote along with all the details about that particular thought

soup = BeautifulSoup(allquotes, "html.parser")
quotes = soup.select('.quote')
formatted_quotes = list()

for quote in quotes:
    quote_text = quote.select(".text")[0].get_text()
    quote_author = quote.select(".author")[0].get_text()
    author_url = quote.select("[href]")[0].attrs['href']
    single_quote = dict(
        quote=quote_text, author=quote_author, link=author_url)
    formatted_quotes.append(single_quote)

# Choose one dictionary(quote) randomly from the list - , when qoute is chosen, reach out to the author page and get
# several hints concerning the author of this quote

quote_question = random.choice(formatted_quotes)
print(quote_question)

# prompt the user to guess who this quote is from

# decrease a counter for every wrong guess

# After each wrong guess, reach out to the author bio page (through the bio link stored in the dictionary) and give hints

# If user guesses incorrectly to the end, end game and give them the answer, also ask if they would like to play again, choose another random quote and start again

# If user guesses correctly within the allowed 4 guesses, stop the game, inform the user that they have won and prompt them if they would like to play again.
