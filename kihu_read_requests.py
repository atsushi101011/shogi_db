from time import sleep
import pandas as pd

from bs4 import BeautifulSoup
import requests



url = 'https://shogidb2.com/latest/page/{}'
d_list = []

for i in range(1,3):
    target_url = url.format(i)
    r = requests.get(target_url)
    sleep(1)

    soup = BeautifulSoup(r.text,'html.parser')
    print(soup)

    contents = soup.find_all('a', class_='list-group-item')
    print(content.text)

    '''for content in contents:
        detail = content.find('div', class_='w-100')

        tournament = detail.find('p').text
        first_move = detail.find('p', class_='h5')[0].text
        second_move = detail.find('p', class_='h5')[1].text
        tactics = detail.find('p', class_='text-right').text
        kihu_url = content.find('a').get('href')

        d = {
            '先手': first_move,
            '後手': second_move,
            'tournament': tournament,
            'tactics': tactics,
            'kihu_url': kihu_url
        }
        d_list.append(d)
        sleep(2)

df = pd.DataFrame(d_list)
df.to_csv('kihu_urls_20221017.csv')'''