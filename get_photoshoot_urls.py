from bs4 import BeautifulSoup
from requests import Session
import requests

url="https://hqdiesel.net/thumbnails.php?album="
for i in range(1,3432):#3432
    uurl=url+str(i)
    r=requests.get(uurl)
    bs = BeautifulSoup(r.content, 'html.parser')
    page_title =bs.title.string
    # if page_title.split(" ")[1].startswith("Error") or not page_title.split("(")[1].startswith("Photoshoots"):
    if not page_title.split("(")[-1].startswith("Photoshoots"):
        continue
    print(uurl)