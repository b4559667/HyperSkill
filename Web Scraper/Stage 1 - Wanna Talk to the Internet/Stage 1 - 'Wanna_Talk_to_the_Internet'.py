import requests

user_input = input("Enter URL: ")
request = requests.get(user_input)
if request.status_code != 200 or "content" not in request.json():
    print("Invalid quote resource!")
else:
    print(request.json().get("content"))