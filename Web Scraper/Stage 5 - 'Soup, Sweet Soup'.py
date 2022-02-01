import requests
from string import punctuation
from bs4 import BeautifulSoup
import os


def soup_sweet_soup(number_of_pages, type_of_articles):
    link_list = []
    if type_of_articles == "Article":
        pass
    else:
        type_of_articles = type_of_articles.upper()
    for page in range(1, number_of_pages + 1):  # Starts loop and iterates from page 1 to specified number
        link = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={}".format(page)
        os.mkdir("Page_{}".format(page))
        soup = BeautifulSoup(requests.get(link).content, "html.parser")
        for article in soup.find_all("a", "c-card__link u-link-inherit"):  # Scrapes all article links
            href_value = (article.get("href"))
            if BeautifulSoup(requests.get("https://www.nature.com" + href_value).content, "html.parser").find("li",
                                                                                                              "c-article-identifiers__item").get_text() == type_of_articles:
                link_list.append("https://www.nature.com" + href_value)
        for link_ in link_list:
            title = str(BeautifulSoup(requests.get(link_).content, "html.parser").find("h1").get_text())
            if type_of_articles != "Article":
                article_text = BeautifulSoup(requests.get(link_).content, "html.parser").find("div",
                                                                                              "c-article-body u-clearfix").text
            else:
                article_text = BeautifulSoup(requests.get(link_).content, "html.parser").find("div",
                                                                                              "c-article-section__content").text
            for i in title:
                if i in punctuation:
                    title = title.replace(i, "")
                if i == " ":
                    title = title.replace(" ", "_")
            title = title + ".txt"
            path = os.path.join(
                r'C:\\Users\\TheAnimeHunter2076\\PycharmProjects\\Web Scraper\\Web Scraper\\task\\Page_{}'.format(page),
                title)
            file = open(path, "w", encoding="utf-8")
            file.write(article_text.strip())
            file.close()
    return 0


input_number = int(input("Enter number of pages: "))
input_title = input("Enter article type:")
test = soup_sweet_soup(input_number, input_title)