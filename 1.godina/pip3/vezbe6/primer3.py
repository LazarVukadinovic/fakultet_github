import requests as req

link = 'https://imi.pmf.kg.ac.rs'
REQ_TYPE = 'GET'
CHUNK_SIZE = 100_000

response = req.request(REQ_TYPE, link)

if response.status_code == req.codes.ok:
    with open('imi.html', 'wb') as writer:
        for chunk in response.iter_content(CHUNK_SIZE):
            writer.write(chunk)

