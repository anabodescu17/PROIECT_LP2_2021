import requests
from bs4 import BeautifulSoup

URL = 'https://xpage.primariatm.ro/lotusweb.nsf/autorizatiiurbanism.xsp'
my_headers = {"User-Agent": "Mozilla/5.0"}
page = requests.get(URL, headers=my_headers)
soup = BeautifulSoup(page.content, 'html.parser')

a = soup.find('tbody')
b = a.find_all('tr', role="row")
"""
print(b[0])
print(b[0].find(style="font-family:Courier New CE;font-size:10pt").get_text())
print(b[0].find(style="font-weight:bold").get_text())
print(b[0].find(class_='xspColumnViewEnd').get_text())
"""
Nr_Data = [item.find(style="font-family:Courier New CE;font-size:10pt").text for item in b]
Beneficiar = [item.find(style="font-weight:bold").text for item in b]
Descriere = [item.find(class_='xspColumnViewEnd').text for item in b]

print(Nr_Data)
print(Beneficiar)
print(Descriere)
