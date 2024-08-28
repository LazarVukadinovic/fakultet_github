import bs4
import requests as req
import webbrowser

parametar = input("Unesite parametar: ").strip()
LINK = 'https://google.com/search?q=' + parametar
REQ_TYPE = 'GET'
MAX_SIZE = 100_000
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
}
response = req.request(REQ_TYPE, LINK, headers=headers)

# if response.status_code == req.codes.ok:
#     with open('stranica.html', 'wb') as writer:
#         for chunk in response.iter_content(MAX_SIZE):
#             writer.write(chunk)

if response.status_code == req.codes.ok:
    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    print(soup.text)
    for link in soup.select('h2 > a')[:10]:
        print(f'Link: {link.get('href')}')
        webbrowser.open(link.get('href'))