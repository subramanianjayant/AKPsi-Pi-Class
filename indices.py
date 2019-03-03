from urllib.request import urlopen
from bs4 import BeautifulSoup

tickers = ['$DOWI','NDAQ','$SPX','VTWO','HSH19','NYH19','PRFZ', 'DAX']

def get_soup(url):
	return BeautifulSoup(urlopen(url),'html.parser')

def get_stats(ticker):
	#url = 'https://www.cnbc.com/quotes/?symbol=.'+ticker
	url = 'https://www.barchart.com/stocks/quotes/'+ticker+'/technical-analysis'
	soup = get_soup(url)
	dict = eval(soup.find(class_ = 'page-title').get('data-ng-init')[5:-1])
	mov_avg = [td.findAll(class_ = 'up') for td in soup.findAll('tr',{'class':'odd'})][1][0].get_text()
	price = dict['lastPrice']
	price_chng = dict['priceChange']
	price_pct = dict['percentChange']
	return (str(ticker+':\t'+str(price)+' | '+str(price_chng)+' | '+str(price_pct)+' | '+str(mov_avg)))

stats = [get_stats(ticker) for ticker in tickers]

print('price | \t change | \t % change | \t 50 day MA')
for s in stats:
	print(s)
