import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.johnlewis.com/samsung-addwash-ww90k5410ww-eu-washing-machine-9kg-load-a-energy-rating-1400rpm-spin-white/p2523271"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}

response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

pattern = re.compile(r"(\d+,?\d+\.\d\d)")
match = pattern.search(string_price)
found_price = match.group(1)
without_commas = found_price.replace(",", "")
price = float(without_commas)

print(price)