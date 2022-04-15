import pandas as pd

import os
import re
from datetime import datetime
import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

class BookDBUpdater:

    def __init__(self):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver.exe'), chrome_options=chrome_options)
        self.metaData = pd.read_csv('UpdaterMetaData.csv')

    def metaDataUpdate(self, column, value):
        
        self.metaData[column] = [value]
        self.metaData.to_csv('UpdaterMetaData.csv', encoding='utf-8', index=False)


    def getCode(self):
        # 알라딘 사이트의 도서 분야 코드를 수집

        # 날짜 비교 하는 게 의미가 있을까?
        # metaData의 CodeUpdate와 비교해서 코드 수행
        today = time.strptime(datetime.today().strftime("%Y/%m/%d"), "%Y/%m/%d")
        metaDay = time.strftime(self.metaData['CodeUpdate'][0], "%Y/%m/%d")
        
        if today < metaDay:
            return

        codes = pd.DataFrame(columns=['code', 'name'])

        self.driver.get("https://www.aladin.co.kr/home/wbookmain.aspx")
        html = self.driver.page_source
        self.driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        
        browse_sub_list = soup.select('li.browse_sub > a')

        #extract href and text
        for li in browse_sub_list:
            codes = codes.append({'code':li.attrs['href'].split('=')[1], 'name': li.text}, ignore_index=True)
        
        #save to csv
        codes.to_csv('codes.csv', encoding='utf-8', index=False)

        #update metadata 
        self.metaDataUpdate('CodeUpdate', datetime.today().strftime("%Y/%m/%d"))

    def getBookURL(self, code):
        # url만 수집? url 타고 들어가서 data 다 수집??? 흠...
        
        self.driver.get('')

    

if __name__ == "__main__":

    getbook = BookDBUpdater()
    getbook.getCode()
    