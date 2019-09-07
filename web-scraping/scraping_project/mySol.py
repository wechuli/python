from bs4 import BeautifulSoup
import time
import requests
import random


# the base url

base_url = "http://quotes.toscrape.com"

# get all the html for the quotes

page = 1
allquotes = ""
while True:
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


# prompt the user to guess who this quote is from


while True:

    quote_question = random.choice(formatted_quotes)
    author = quote_question.get('author')
    author_link = quote_question.get('link')
    print(author)
    print('..............................................')
    print(quote_question.get('quote'))
    user_guess = input("Who said the above quote: ")
    if user_guess == quote_question.get('author'):
        print(f'You are right, {author} said it!')
        play_again = input("Do you want to play again? y or n: ")
        if play_again == 'y':
            continue
        else:
            break

    else:
        author_details_raw = requests.get(
            f'http://quotes.toscrape.com{author_link}').text
        author_soup = BeautifulSoup(author_details_raw, 'html.parser')

        author_dob = author_soup.select('.author-born-date')[0].get_text()
        author_birth_location = author_soup.select(
            '.author-born-location')[0].get_text()
        author_first_name = author_soup.select(
            '.author-title')[0].get_text().split(' ')[0]
        author_last_name = author_soup.select(
            '.author-title')[0].get_text().split(' ')[1]
        


        while number_of_guesses < 4:
            # store the hints in a list and each time, move through them and if 

            # decrease a counter for every wrong guess

            # After each wrong guess, reach out to the author bio page (through the bio link stored in the dictionary) and give hints

            # If user guesses incorrectly to the end, end game and give them the answer, also ask if they would like to play again, choose another random quote and start again

            # If user guesses correctly within the allowed 4 guesses, stop the game, inform the user that they have won and prompt them if they would like to play again.
