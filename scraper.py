#Will use requests// no java so sodium is over
import requests
from bs4 import BeautifulSoup

page = requests.get('https://quotes.toscrape.com/')
print(page)

