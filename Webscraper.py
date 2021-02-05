import requests
from bs4 import BeautifulSoup

print("\nPlease input a ticker you would like to search\n")

Ticker = input()

URL = 'https://finance.yahoo.com/quote/' + Ticker + '?'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="quote-header-info")
stockprice = results.find_all('div', class_='D(ib) Mend(20px)')

for stockprice in stockprice:
    print('\n',stockprice.text, end='\n'*2)