import requests
from bs4 import BeautifulSoup

site = 'https://www.foxnews.com/'

r = requests.get(site)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
images = soup.findAll('img')
for image in images:
    #print image source
    print(image['src'])
    #print alternate text
    print(image['alt'])
