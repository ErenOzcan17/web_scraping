from bs4 import BeautifulSoup
import requests

url = 'https://tr.wikipedia.org/wiki/Python'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title')
print(title.text)
"--------------------------"

ilk_paragraf = soup.find('p').text
print("ilk_paragraf : " + ilk_paragraf)

"--------------------------"

for paragraf in soup.find_all('p'):
    print(paragraf.text)

"--------------------------"
content = soup.select('[id^=toc-]')
for items in content:
    print(items.text)

"--------------------------"
tables = soup.find_all('table')
for table in tables:
    print("tablo başlığı")
    table_title = table.caption.text if table.caption else "Tablo başlığı yok"
    print(table_title)

    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all(['th', 'td'])
        for cell in cells:
            print(cell.text.strip(), end="\t")
        print()

"--------------------------"
import os
from urllib.parse import urljoin

images = soup.find_all('img')
os.makedirs('images', exist_ok=True)
for index, image in enumerate(images):
    image_url = image['src']
    if image_url.startswith('//'):
        image_url = 'https:' + image_url
    if not image_url.startswith(("http://", "https://")):
        image_url = 'https://tr.wikipedia.org' + image_url
        image_url = urljoin(url, image_url)
    with open (f'images/{index}.jpg', 'wb') as file:
        file.write(requests.get(image_url).content)
    alt_text = image['alt'] if 'alt' in image.attrs else 'No alt text.'
    print(f"image {index} url si : {image_url}")
    print(f"image {index} alt text : {alt_text}")