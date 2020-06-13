import requests 
from urllib.request import urlopen # open URLs
from bs4 import BeautifulSoup # BeautifulSoup; parsing HTML
import re # regex; extract substrings
from datetime import datetime # calculate script's run time

print("Starting...")
start = datetime.now()

page_url = 'https://www.claritine.pl/pl/prognoza-dla-alergikow/aktualna-prognoza-pylenia/?region=5'

page = urlopen(page_url)
soup = BeautifulSoup(page, 'html.parser') # parse the page

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

# get description
description = soup.find("div", {"class":"description"})
description = str(description)
description = re.search(r'(<p>(.|\n)*?<\/p>)', description)
description = description.group(0)
description = str(cleanhtml(description))
description = description.strip()

print("Description MZ:", description)
with open(r"allergens-description-R5MZ.txt", "w", encoding="utf-8") as file:
    file.write(description)