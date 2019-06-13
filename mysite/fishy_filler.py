from bs4 import BeautifulSoup
import requests
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from fish.models import Fish


def get_fish():
    result = requests.get('https://nookipedia.com/wiki/Fish/Animal_Crossing:_New_Leaf')
    c = result.content
    soup = BeautifulSoup(c, 'html.parser')
    table_rows = soup.find_all('tr')

    all_rows = []
    for unfiltered_row in table_rows:
        new_row = []
        for data in unfiltered_row.find_all('td'):
            if data.find('img') and 'Coconut' not in data.find('img')['src']:
                image = "https://nookipedia.com" + data.find('img')['src']
                new_row.append(image)
            else:
                new_row.append(data.get_text().strip().replace('\n', ''))
        all_rows.append(new_row)

    # removes the empty header
    all_rows.pop(0)

    # this is taking out all of the stuff that don't really make sense
    # removes 'average', 'tank', 'months' columns
    # also parses the appropriate data to ints
    for row in all_rows:
        del row[5]
        del row[5]
        del row[-1]
        row[0] = int(row[0])
        row[3] = int(row[3].replace(',', ''))

    # fish 'Coelacanth' has a 1 at the end of its location. Should just be 'Ocean'
    # changed inside the admin

    return all_rows


def populate(rows):
    for row in rows:
        fish = Fish.objects.get_or_create(name=row[1], image=row[2], price=row[3],
                                  shadow=row[4], location=row[5], time=row[6])[0]


if __name__ == '__main__':
    print("getting the fishies")
    all_fish = get_fish()
    print("putting all the fishies in teh db")
    populate(all_fish)
    print("the fishies are finished")