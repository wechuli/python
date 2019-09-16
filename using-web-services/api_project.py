import colorama
import requests
import pprint
from termcolor import colored
from pyfiglet import figlet_format
colorama.init()


welcome_msg = "Dad Jokes 101"
fancy_msg = figlet_format(welcome_msg)
base_url = 'https://icanhazdadjoke.com/search'

print(colored(fancy_msg, color='green'))

search_term = input("Let's make jokes! Give me a topic: ")


response = requests.get(
    base_url, headers={'Accept': 'application/json'}, params={"term": search_term, "limit": 20})

data = response.json()


if data['results']:
    if len(data['results']) == 1:
        print(
            f'Great, I have 1 joke about "{search_term}", here it is')
        joke = data['results'][0]['joke']
        print(colored(joke, color='cyan'))
    else:
        joke_no = len(data['results'])
        print(
            f'Great, I have {joke_no} jokes about "{search_term}", here they are')
        print(colored('------------', color='red'))
        for item in data['results']:
            joke = item['joke']
            print(colored(joke, color='cyan'))
            print(colored('------------', color='red'))

else:
    print(f'Sorry buddy, no jokes for "{search_term}"')
