import requests
from bs4 import BeautifulSoup

URL = 'https://xpage.primariatm.ro/lotusweb.nsf/autorizatiiurbanism.xsp'

my_headers = {"User-Agent": "Google Chrome/12.7"}

page = requests.get (URL, headers=my_headers)
soup = BeautifulSoup (page.content, 'html.parser')

Beneficiar = soup.find_all ('td', style='font-weight:bold')  # afiseaza continutul coloanei 2
for i in Beneficiar:
    print (i.text)
