import requests
from bs4 import BeautifulSoup

URL = 'https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="quote-header-info")
stockprice = results.find_all('div', class_='D(ib) Mend(20px)')

for stockprice in stockprice:
    print(stockprice.text, end='\n'*2)