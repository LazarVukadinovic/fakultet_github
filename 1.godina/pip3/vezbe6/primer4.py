import bs4
import requests as req

# Prvi nacin - lokalni fajl
with open('./vezbe6/imi.html', 'rb') as reader:
    soup = bs4.BeautifulSoup(reader.read(), features='html.parser')


# Drugi nacin - link
link = 'https://imi.pmf.kg.ac.rs'
response = req.request('GET', link)

if response.status_code == req.codes.ok:
    soup = bs4.BeautifulSoup(response.text, features='html.parser')