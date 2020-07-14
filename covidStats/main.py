from functools import reduce
from bs4 import BeautifulSoup
import requests

country = input("Choose a country to get coronavirus stats\n> ")
countryURL = country.lower().replace(" ", "-")

url = f"https://www.worldometers.info/coronavirus/country/{countryURL}/"
r = requests.get(url)
page = BeautifulSoup(r.content, "html5lib")

if page.title.getText() == "404 Not Found":
  print("Invalid country name")
  exit()

stats = {tag.h1.getText(): tag.div.span.getText().replace(",", "") 
        for tag in page.findAll("div", attrs={"id":"maincounter-wrap"}) if tag.h1}
stats["Active:"] = reduce(lambda x, y: int(x)-int(y), stats.values())

print(f"\n{country.upper()}")
for key, value in stats.items():
  print(f"{key} {int(value):,}")