import requests
from bs4 import BeautifulSoup
import re

URL = 'https://xpage.primariatm.ro/lotusweb.nsf/autorizatiiurbanism.xsp'
my_headers = {"User-Agent":"Chrome/5.0"}
page = requests.get(URL, headers = my_headers)
soup = BeautifulSoup(page.content, 'html.parser')

'''Nr_Data = re.findall(r'\d\d\d/\d\d.\d\d.\d\d\d\d', soup.prettify())           !!!nu mai e valabil
print(soup.prettify())  #afiseaza continutul paginii html
for nr in Nr_Data:
   print(nr)
'''

NrData = soup.find_all('td', style = 'font-family:Courier New CE;font-size:10pt')
for i in NrData:
    print(i.text)