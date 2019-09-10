import requests
import time
from random import choice

from bs4 import BeautifulSoup
base_url = 'http://quotes.toscrape.com'


def scrape_quotes():
    all_quotes = []

    url = "/page/1"

    while url:

        res = requests.get(f'{base_url}{url}')
        print(f'scraping the {base_url}{url} ')
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        # time.sleep(1)
    return all_quotes

all_quotes = scrape_quotes()

def start_game():
    quote = choice(all_quotes)

    remaining_gueses = 4
    guess = ''
    print(quote["author"])
    print(quote["text"])

    while guess != quote['author'].lower() and remaining_gueses > 0:
        guess = input(
            f"Who said this quote? Guesses remaining:{remaining_gueses}: ")
        remaining_gueses -= 1
        if guess.lower() == quote["author"].lower():
            print("You got it right")
            break
        if remaining_gueses == 3:
            res = requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(
                f"Here is a hint: The author was born on {birth_date} {birth_place}")
        elif remaining_gueses == 2:
            first_name = quote["author"][0]
            print(
                f"Here is a hint: The author's first name starts with {first_name}")
        elif remaining_gueses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(
                f"Here is a hint: The author's last name starts with {last_initial}")
        else:
            print(
                f"Sorry ypou ran out of guesses . The answer was {quote['author']}")

    again = ""
    while again not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play agin(y/n)")
        if again.lower() in ("yes", "y"):
            return start_game()
        else:
            print("Ok, goodbye")


start_game()
