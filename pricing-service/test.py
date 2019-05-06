import requests

response = requests.get("https://www.johnlewis.com/samsung-addwash-ww90k5410ww-eu-washing-machine-9kg-load-a-energy-rating-1400rpm-spin-white/p2523271")

print(response.content)