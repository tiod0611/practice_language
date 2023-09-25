'''
퀴즈. 네이버에서 부동산 정보를 검색하여 나오는 결과를 출력하자.

출력 예시

======== 매물 1 =========
거래 : 매매
면적 : 84/59(공급/전용)
가격 : 165,000 (만원)
동 : 214동
층 : 고/23
======== 매물 2 =========
....

'''

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import chromedriver_autoinstaller

import time

user_agent = generate_user_agent(os='win', device_type='desktop')

options=ChromeOptions()
options.add_argument(f'user_agent={user_agent}')

driver_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(driver_path, options=options)
driver.maximize_window()

# 검색 문구
search_word = '송파 헬리오시티'

# url 접속
driver.get("https://land.naver.com/")
search_area = driver.find_element(By.XPATH, '//*[@id="queryInputHeader"]')
search_area.send_keys(search_word)
search_area.send_keys('\n')
time.sleep(1)

# 매물 정보 크롤링
soup = BeautifulSoup(driver.page_source, 'lxml')

item_list = soup.find_all('div', attrs={'class':'item_inner'})

for i, item in enumerate(item_list):

    dong = item.find('span', attrs={'class':'text'}).text.split(' ')[-1]
    item_type = item.find('span', attrs={'class':'type'}).text
    price = item.find('span', attrs={'class':'price'}).text.replace('\n', ' ')
    spec = item.find('span', attrs={'class':'spec'}).text.replace(',', '').split(' ')
    floor = spec[1]
    area = spec[0]
    direction = spec[2]
    
    print(f'======== 매물 {i} =========')
    print("거래 : {}".format(item_type))
    print("면적 : {}(공급/전용)".format(area))
    print("가격 : {}".format(price))
    print("동 : {}".format(dong))
    print("층 : {}(해당층/총층)".format(floor))
    print("방향 : {}".format(direction))



