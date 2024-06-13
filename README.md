
## Steps to install:
### 1.Create python venv
```python
python -m venv hqdiesel-scraper
```
### 2.Click on bs4.bat
A terminal will get opened like
`(hqdiesel-scraper) C\...\hqdiesel-scraper>`
```
pip install -r requirements.txt
```
### 3.Running script
```
python scrape.py
```
took reference from this repo for main code(https://github.com/falcon883/hqdiesel-album-scraper)

## scrape_photoshoots_only.py 
**Purpose**:It will filter photoshoot only albums from given range of albums mentioned inside the script file and download automatically.
```
python scarpe_photoshoots_only.py
```
*Don't forget to edit range inside script*

## get_photoshoot_urls.py
**Purpose**:It will print photoshoot only album urls on console without downloading.
```
python get_photoshoot_urls.py
```
OR
to save urls in file
```
python get_photoshoot_urls.py >> photoshoot_urls.txt
```

## check_female.py
**Purpose**:It will filter links for only female photoshoot albums.(*you can edit url inside script for custom filter,refer hqdiesel website.*)
```
python check_female.py
```
OR
to save urls in file
```
python check_female.py >> female_photoshoot_urls.txt
```

## get_names.py
**Purpose**:It will check urls got from `get_photoshoot_urls.py` and print names,file number and pages number into a csv file.
```
python get_names.py
```

## DATA Folder
It contains data I extracted during testing

## Random.bat (Windows)(Offline)
Just a Pseudo-random generator between 1-540

## cleanup.bat (Windows)(Offline)
Cleans the Downloaded Photoshoot album Folders including images inside it.

## bs4.bat (Windows)(Offline)
Just a faster venv launcher

