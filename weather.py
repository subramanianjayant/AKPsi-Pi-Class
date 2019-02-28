from urllib.request import urlopen
from bs4 import BeautifulSoup

metar_url = 'https://tgftp.nws.noaa.gov/data/observations/metar/stations/KTEB.TXT'
taf_url = 'https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/KTEB.TXT'

def get_soup(url):
	return BeautifulSoup(urlopen(url),'html.parser')

soup1 = get_soup(metar_url)
soup2 = get_soup(taf_url)

reports = [soup1.prettify(), soup2.prettify()]

for r in reports:
	print(r)

#Prints METAR and TAF reports for station KTEB
