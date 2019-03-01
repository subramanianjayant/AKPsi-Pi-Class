from urllib.request import urlopen
from bs4 import BeautifulSoup

tickers = ['DJI','IXIC','SPX','RUT','HSI','N225','FTSE', 'DAX']

def get_soup(url):
	return BeautifulSoup(urlopen(url),'html.parser')

stats = []

for ticker in tickers:
	url = 'https://www.cnbc.com/quotes/?symbol=.'+ticker
	soup = get_soup(url)
	price = soup.find(itemprop = 'price').get('content')
	price_chng = soup.find(itemprop = 'priceChange').get('content')
	price_pct = soup.find(itemprop = 'priceChangePercent').get('content')
	stats.append(str(ticker+':\t'+str(price)+' | '+str(price_chng)+' | '+str(price_pct)))

for s in stats:
	print(s)
