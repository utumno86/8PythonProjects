__author__ = 'utumno86'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-gramercy-chair-black/p3314947")

content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", { "class": "price--large"})
string_price = element.text.strip()
price = float(string_price[1:])

print("The current price is {}".format(string_price))
if price > 200:
  print("Chair is too expensive")
else:
  print("Buy the chair")
