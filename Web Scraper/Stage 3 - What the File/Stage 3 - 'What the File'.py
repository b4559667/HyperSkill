import requests

user_input = input("Enter URL: ")
if requests.get(user_input).status_code in range(200, 300):
    page_content = requests.get(user_input).content
    file = open("source.html", "wb")
    file.write(page_content)
    print("Content saved.")
else:
    print("The URL returned {}".format(requests.get(user_input).status_code))