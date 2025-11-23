import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")
data = []

for q in quotes:
    quote_text = q.find("span", class_="text").get_text(strip=True)
    author = q.find("small", class_="author").get_text(strip=True)
    data.append([quote_text, author])

for item in data:
    print(item)

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(data)

print("Data successfully saved to quotes.csv")
