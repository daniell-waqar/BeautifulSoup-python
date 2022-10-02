import  requests

from bs4 import  BeautifulSoup

url = "https://www.theboutiqueasia.com/collections/shirts"

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

main = soup.findAll('div', {"class": "product-layout"})


for data in main:

    price = data.find('p',{'class':"price"})
    print(price.text)

    name = data.find('h4')
    print(name.text)