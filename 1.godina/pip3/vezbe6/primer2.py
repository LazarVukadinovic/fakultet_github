import requests as req

link = 'https://imi.pmf.kg.ac.rs'
response = req.request('GET', link)
print(f'Statusni kod: {response.status_code}')
print(f'Tekst: \n{response.text}')