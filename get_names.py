from bs4 import BeautifulSoup
from requests import Session
import requests
import csv

Filepath=input("Enter Path:")
with open(Filepath) as file:
    for item in file:
        r=requests.get(item)
        bs = BeautifulSoup(r.content, 'html.parser')
        tables = bs.find_all('table', {'class': 'maintable'})
        #finding names
        names = tables[0].find_all('a', href=True)[3].string
        # finding files
        tds = bs.find_all('td',{'class': 'tableh1'})
        files = tds[2].string.split(" ")
        file = files[0]
        #finding pages
        pages = files[3]
    #writing to file
        List = [names,file,pages]
        fields=['name','files','pages']
        print(item)
        print(List)
        with open(r'album_names.csv', 'a' ,encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(List)