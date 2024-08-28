import bs4
import requests as req

link = 'https://imi.pmf.kg.ac.rs'
REQ_TYPE = 'GET'
response = req.request(REQ_TYPE, link)

if response.status_code == req.codes.ok:
    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    print(f'Naslov stranice {soup.title.text}')

    links = soup.find_all('a')
    for link in links:
        print(f'Link: {link.get('href')}')
        print(f'Text linka: {link.get_text().strip()}\n')