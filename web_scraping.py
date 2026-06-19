import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

df = pd.DataFrame(quotes, columns=["Quote"])

df.to_csv("data/quotes.csv", index=False)

print("Data Saved Successfully")