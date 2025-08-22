import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.passiton.com/inspirational-quotes"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

quotes_baner = soup.find_all("div", class_="col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top")
quotes = []

for q in quotes_baner:
    quote_text = q.img.get("alt").split("#")
    image_url = q.img.get("src")
    theme = q.h5.a.text.capitalize()
    quote = {
        "theme": theme,
        "image_url": image_url,
        "text": quote_text[0],
        "author": quote_text[1]
    }
    quotes.append(quote)

filename = "quotes.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["theme", "image_url", "text", "author"])
    writer.writeheader()

    for quote in quotes:
        writer.writerow(quote)


