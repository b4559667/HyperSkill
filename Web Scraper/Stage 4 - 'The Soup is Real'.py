import requests
from string import punctuation
from bs4 import BeautifulSoup

news_ = []
user_input = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
soup = BeautifulSoup(requests.get(user_input).content, "html.parser")
for article in soup.find_all("a", "c-card__link u-link-inherit"):
    tmp = (article.get("href"))
    if BeautifulSoup(requests.get("https://www.nature.com" + tmp).content, "html.parser").find("li",
                                                                                               "c-article-identifiers__item").get_text() == "NEWS":
        news_.append("https://www.nature.com" + tmp)
for link in news_:
    title = str(BeautifulSoup(requests.get(link).content, "html.parser").find("h1").get_text())
    article_text = BeautifulSoup(requests.get(link).content, "html.parser").find("div",
                                                                                 "c-article-body u-clearfix").text
    for i in title:
        if i in punctuation:
            title = title.replace(i, "")
        if i == " ":
            title = title.replace(" ", "_")
    title = title + ".txt"
    file = open(title, "w", encoding="utf-8")
    file.write(article_text.strip())