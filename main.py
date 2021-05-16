import requests
from bs4 import BeautifulSoup
import pandas
import re


URL = 'https://xpage.primariatm.ro/lotusweb.nsf/autorizatiiurbanism.xsp'
my_headers = {"User-Agent": "Mozilla/5.0"}
page = requests.get(URL, headers=my_headers)
soup = BeautifulSoup(page.content, 'html.parser')

tbody = soup.find("tbody")
columns = []
for tr in tbody.find_all('tr'):
    columns.append([tr.text for tr in tr.find_all("td")])
columns = list(zip(*columns))


print(columns[0])
print(columns[1])
print(columns[2])
print(columns[3])

numar_strada = []
nume_strada = []
for i in columns[2]:
    numar = re.search(r"(nr.+)", i)

    nume = re.search(r".+?(?=nr)", i)
    if numar:
        numar_strada.append(numar.group())
    if nume:
        nume_strada.append(nume.group())
print(nume_strada)
print(numar_strada)
