import requests
from bs4 import BeautifulSoup

URL = 'https://xpage.primariatm.ro/lotusweb.nsf/autorizatiiurbanism.xsp'

my_headers = {"User-Agent":"Chrome/5.0"}

page = requests.get(URL, headers = my_headers)
soup = BeautifulSoup(page.content, 'html.parser')

a = soup.find('tbody')
b = a.find_all('tr',role="row")
#print(b[0].find(style="").get_text())

Adresa_lucrarii  = [item.find(style="").text for item in b]
print(Adresa_lucrarii)