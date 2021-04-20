import requests
from bs4 import BeautifulSoup
URL = 'https://xpage.primariatm.ro/lotusweb.nsf/autorizatiiurbanism.xsp'

my_headers = {"User-Agent":"Opera GX/72.3"}

page = requests.get(URL, headers=my_headers)
soup = BeautifulSoup(page.content, 'html.parser')

Descriere= soup.find_all( class_ = 'xspColumnViewEnd') #afiseaza continutul coloanei 4
for i in Descriere:
    print(i.text)