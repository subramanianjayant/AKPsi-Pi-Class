from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.aviationweather.gov/taf/board?ids=KJFK'

def get_soup(url):
	return BeautifulSoup(urlopen(url),'html.parser')

soup = get_soup(url)

box1 = soup.find('code')
print(box1) #Prints raw html for TAF
