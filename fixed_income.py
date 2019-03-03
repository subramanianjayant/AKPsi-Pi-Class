from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas_datareader as pdr

def get_soup(url):
	return BeautifulSoup(urlopen(url),'html.parser')

treasury_url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield'
soup = get_soup(treasury_url)
treasury_rates = [r.get_text() for r in soup.findAll(class_='text_view_data')[1:]]
print(treasury_rates)

mortgage_url = 'https://www.quickenloans.com/mortgage-rates#chat_close'
soup = get_soup(mortgage_url)
mort_rates_APR = soup.findAll('p',{'class':'b-Heading--secondary'})
mort_rates = {}
mort_rates['15 yr fixed'] = mort_rates_APR[0].get_text()
mort_rates['30 yr fixed'] = mort_rates_APR[2].get_text()
mort_rates['5 yr arm'] = mort_rates_APR[4].get_text()
mort_rates['30 yr fixed FHA'] = mort_rates_APR[6].get_text()
mort_rates['30 yr fixed VA'] = mort_rates_APR[8].get_text()
print(mort_rates)
