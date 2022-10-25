import requests

from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url).text
#print(response)

soup = BeautifulSoup(response, "html.parser")

price = soup.findAll('p', {'class':"price_color"})
for i in price:
    print(i.text)

name = soup.findAll('h3')
for j in name:
    print(j.text)

link = soup.findAll('div', {'class':"image_container"})

for k in link:
    li = k.find('a')['href']
    print(li)