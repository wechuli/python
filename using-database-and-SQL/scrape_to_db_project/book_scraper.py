
import requests
from bs4 import BeautifulSoup


def scrape_books():
        # request URL
    response = requests.get(
        "http://books.toscrape.com/catalogue/category/books/history_32/index.html")
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article")
    all_books = []
    for book in books:
        title = get_title(book)
        price = get_price(book)
        rating = get_rating(book)
        all_books.append((title, price, rating))
    return all_books


def get_title(book):
    return book.find("h3").find("a")["title"]


def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("Â", "").replace("£", ""))


def get_rating(book):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    return ratings[rating]
