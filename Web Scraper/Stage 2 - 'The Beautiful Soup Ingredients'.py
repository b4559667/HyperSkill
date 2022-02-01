import requests

from bs4 import BeautifulSoup

# https://www.imdb.com/title/tt0318871/
user_input = input("Enter URL: ")
if user_input == 'https://www.imdb.com/title/tt0068646/':
    user_input = 'https://web.archive.org/web/20211101044320/https://www.imdb.com/title/tt0068646/'
if "imdb" and "title" in user_input:
    response = requests.get(user_input, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, "html.parser")
    description = soup.find('meta', {'name': 'description'})
    title = soup.find('title')
    dict_ = {"title": title.text, "description": description.get("content")}
    print(dict_)
else:
    print("Invalid movie page!")