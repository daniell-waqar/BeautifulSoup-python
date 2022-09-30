
import requests
from bs4 import BeautifulSoup

url = "https://www.thewhiskyexchange.com/p/66727/foursquare-elysium-12-year-old-exclusive-to-the-whisky-exchange"

html = requests.get(url).text


soup = BeautifulSoup(html, 'html.parser')
name = soup.find('h1')
print(name.text)

price = soup.find('p', {'class': "product-action__price"})
print(price)

rate = soup.find('span', {'class': 'review-overview__count'})
print(rate)


