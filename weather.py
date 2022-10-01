import requests
from bs4 import BeautifulSoup

url = ('https://forecast.weather.gov/MapClick.php?lat=34.09927000000005&lon=-118.33806999999996#.XIRJ81NKgUE')

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

main = soup.find(id="seven-day-forecast-body")
print(main.text, "/n")
