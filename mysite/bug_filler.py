from bs4 import BeautifulSoup as bs
import requests
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from bugs.models import Bug


result = requests.get('https://nookipedia.com/wiki/Bugs/Animal_Crossing:_New_Leaf')
c = result.content
soup = bs(c, 'html.parser')
table_rows = soup.find_all('tr')

first_all = []
for unfiltered_row in table_rows:
    new_row = []
    for data in unfiltered_row.find_all('td'):
        if data.find('img') and 'Coconut' not in data.find('img')['src']:
            image = "https://nookipedia.com" + data.find('img')['src']
            new_row.append(image)
        else:
            new_row.append(data.get_text().strip().replace('\n', ''))
    first_all.append(new_row)

first_all.pop(0)

# deleting the extra stuff
for deletion in range(19):
    del first_all[-1]

for td in first_all:
    del td[4]
    del td[4]


# second table
second_result = requests.get('http://www.gamedynamo.com/article/cheats/6174/545/en/nintendo_3ds/animal_crossing_new_leaf')
second_c = second_result.content
second_soup = bs(second_c, 'html.parser')
table = second_soup.find('table', {'class': 'table_n3ds'})

for deletion in range(3):
    del table[0]

second_all =[]
for row in table.find_all('tr'):
    new_row = []
    for td in row.find_all('td'):
        new_row.append(td.get_text().replace('\n', '').replace('\t', '').replace('*', '').replace('\xa0', ' '))
    second_all.append(new_row)

for tr in second_all:
    print(tr)