from urllib.request import urlopen
from bs4 import BeautifulSoup

tickers = ['DJI','IXIC','SPX','RUT','HSI','N225','FTSE', 'DAX']

def get_soup(url):
	return BeautifulSoup(urlopen(url),'html.parser')

def get_stats(ticker):
	url = 'https://www.cnbc.com/quotes/?symbol=.'+ticker
	soup = get_soup(url)
	price = soup.find(itemprop = 'price').get('content')
	price_chng = soup.find(itemprop = 'priceChange').get('content')
	price_pct = soup.find(itemprop = 'priceChangePercent').get('content')
	return (str(ticker+':\t'+str(price)+' | '+str(price_chng)+' | '+str(price_pct)))

stats = [get_stats(ticker) for ticker in tickers]

for s in stats:
	print(s)
