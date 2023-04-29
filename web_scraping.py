import requests
from bs4 import BeautifulSoup

# input book title
book_title = input("Enter book title: ")

# create search url
url = f"https://myanimelist.net/manga.php?q={book_title.replace(' ', '%20')}&cat=manga"

# make request and parse html
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# extract book url from search results
book_url = soup.find("a", {"class": "hoverinfo_trigger"})["href"] # type: ignore

# make request to book page and parse html
response = requests.get(book_url) # type: ignore
soup = BeautifulSoup(response.content, "html.parser")

# extract score value
score_value = soup.find("span", {"itemprop": "ratingValue"}).text # type: ignore

print(f"The score for {book_title} is {score_value}")
