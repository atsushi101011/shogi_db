from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_path = '/Users/atsushi/Desktop/ScrapingBeginner-main/chromedriver'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
url = 'https://shogidb2.com/latest'
driver.get(url)

sleep(1)

element = driver.find_element_by_class_name('list-group-item')
move = element.find_elements_by_class_name('h5')
first_move = move[0].text
second_move = move[1].text
tournament = element.find_element_by_tag_name('p').text
tactics = element.find_element_by_class_name('text-right').text

print(first_move)
print(second_move)
print(tournament)
print(tactics)

driver.quit()