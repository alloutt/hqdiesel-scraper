from bs4 import BeautifulSoup
from requests import Session
from pathlib import Path
import requests
import shutil
from tqdm.contrib.concurrent import thread_map


url="https://hqdiesel.net/thumbnails.php?album="
for i in range(3431,3432):#3432#range of album number
    uurl=url+str(i)
    r=requests.get(uurl)
    bs = BeautifulSoup(r.content, 'html.parser')
    page_title =bs.title.string
    if page_title.split(" ")[1].startswith("Error") or not page_title.split("(")[1].startswith("Photoshoots"): # checking for Error pages,filtering only Photoshoots
        continue
    
    #Starts Processing
    tables2 = bs.find_all('table', {'class': 'maintable'})
    for c in tables2[0].find_all('a', href="index.php?cat=230"):
        page_title =bs.title.string.split(" -")[0]
        package_dir = Path(__file__).parent.absolute()
        file_path = package_dir
        file_path = package_dir.joinpath(page_title)
        if not Path.exists(file_path):
            Path.mkdir(file_path)
        tables = bs.find_all('table', {'class': 'maintable'})
        table = tables[1].find('td', {'class': 'navmenu'})
        if table is not None:
                    total_pages = table.find_previous_sibling('td', {'class': 'tableh1'}).text.split()[3]
                    total_pages = int(total_pages)
        image_urls = list()
        for a in tables[1].find_all('a', href=True):
                if str(a['href']).startswith("display"):
                    image_urls.append(f"https://www.hqdiesel.net/gallery/{a['href']}&fullsize=1")
        session = Session()
        def _download_images(pos):
            with session as s:
                try:
                    l = s.get(image_urls[pos])
                    bs2 = BeautifulSoup(l.content, 'html.parser')
                    image_src = bs2.find('div', {'id': 'content'}).find('img')['src']
                    l = s.get(f"https://www.hqdiesel.net/gallery/{image_src}", stream=True)
                    l.raw.decode_content = True
                    with open(f"{file_path}\\{page_title}_{pos}.jpg", 'wb+') as f:
                        shutil.copyfileobj(l.raw, f)
                except Exception as ex:
                    print(ex)
        thread_map(_download_images, range(0, len(image_urls)))