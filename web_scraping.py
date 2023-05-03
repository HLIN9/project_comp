import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_rating(book_title:str):
    # create search url
    url = f"https://myanimelist.net/manga.php?q={book_title.replace(' ', '%20')}&cat=manga"        #########
    #url = f"https://myanimelist.net/anime.php?q={book_title.replace(' ', '%20')}&cat=anime"
    # make request and parse html
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # # extract book url from search results
    # book_url = soup.find("a", {"class": "hoverinfo_trigger"})["href"] # type: ignore

    # # make request to book page and parse html
    # response = requests.get(book_url) # type: ignore
    # soup = BeautifulSoup(response.content, "html.parser")

    try:
        # extract book url from search results
        book_url = soup.find("a", {"class": "hoverinfo_trigger"})["href"] # type: ignore

        # make request to book page and parse html
        response = requests.get(book_url) # type: ignore
        soup = BeautifulSoup(response.content, "html.parser")


        
        # extract score value
        score_value = soup.find("span", {"itemprop": "ratingValue"}).text # type: ignore
    except:
        score_value = 'N/A'
    return score_value

def clean_string(s):
    return ''.join(c for c in s if c.isalnum() or c.isspace())

if __name__ == '__main__':        
    # input book title
    # book_title = input("Enter book title: ")

    with open('text1.txt', 'r') as f1:         ##########
    #with open('text2.txt', 'r') as f1:
        txt_1 = f1.read().lower().splitlines()

    # Create an empty set to store unique, cleaned items
    unique_items = set()

    # Loop through each item in the list
    for item in txt_1:
        # Clean the item by removing non-alphanumeric characters
        cleaned_item = clean_string(item.lower())

        # If the cleaned item is not already in the set, add it
        if cleaned_item not in unique_items:
            unique_items.add(cleaned_item)
    
    unique_items = sorted(list(unique_items))

    # for i in range(len(unique_items)):
    #     print(f"{i+1}. {unique_items[i]}. {get_rating(unique_items[i])}")
    df = pd.DataFrame({'Title': unique_items, 
                       'Rating':[get_rating(str(item)) for item in unique_items]})

    # Print out the contents of df
        # set pandas display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df.sort_values('Rating', ascending=False, na_position='last'))

