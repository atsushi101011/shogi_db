from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_path = '/Users/atsushi/Desktop/ScrapingBeginner-main/chromedriver'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
url = 'https://shogidb2.com/latest/page/{}'
d_list = []

for i in range(1,6):
    target_url = url.format(i)
    driver.get(target_url)

    sleep(2)

    elements = driver.find_elements_by_class_name('list-group-item')

    for element in elements:
        tournament = element.find_element_by_tag_name('p').text
        first_and_second = element.find_elements_by_class_name('h5')
        first_move = first_and_second[0].text
        second_move = first_and_second[1].text
        tactics = element.find_element_by_class_name('text-right').text
        kihu_url = element.get_attribute('href')

        d = {
            '先手': first_move,
            '後手': second_move,
            '棋戦': tournament,
            '戦法': tactics,
            'url': kihu_url
        }
        d_list.append(d)
        sleep(2)

df = pd.DataFrame(d_list)
df.to_csv('kihu_urls_20221017.csv')

driver.quit()