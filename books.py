import requests
from bs4 import BeautifulSoup

url='https://books.toscrape.com/'
response=requests.get(url)
soup= BeautifulSoup(response.text,'html.parser')
#bookshelf=soup.findAll('li', {'class':'col-xs-6 col-sm-4 col-md-3 '})
for item in soup.find_all('article', class_='product_pod'):
    title=item.h3.a.get('title')
    price= item.find('p', class_='price_color').text[1:]
    raiting=item.p['class'][-1]
    print(title, price,  f'Raiting:{raiting}', sep='\n', end='\n\n')
