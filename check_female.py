from bs4 import BeautifulSoup
from requests import Session
import requests


Filepath=input("Enter Links file:")
with open(Filepath) as file:
    for item in file:
        r=requests.get(item)
        bs = BeautifulSoup(r.content, 'html.parser')
        page_title =bs.title.string
        if page_title.split(" ")[1].startswith("Error"):
            continue
        tables = bs.find_all('table', {'class': 'maintable'})
        for a in tables[0].find_all('a', href=True):
            if str(a['href']) == "index.php?cat=230":
                print(item)
