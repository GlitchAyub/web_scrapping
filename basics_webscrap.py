import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.geeksforgeeks.org/')

soup =BeautifulSoup(req.content, "html.parser")

res = soup.title

# prints all the element
# print(soup.prettify())


# prints text presents on that elements
# print(soup.get_text())


print(res.get_text())