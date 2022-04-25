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
        
        user_agent = "user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("--log-level=3")
        self.chrome_options.add_argument('user-agent=' + user_agent)
        
        
    def metaDataUpdate(self, column, value):
        
        metaData = pd.read_csv('UpdaterMetaData.csv')
        metaData[column] = [value]
        metaData.to_csv('UpdaterMetaData.csv', encoding='utf-8', index=False)


    def getCode(self):
        # 알라딘 사이트의 도서 분야 코드를 수집

        # 날짜 비교 하는 게 의미가 있을까?
        # metaData의 CodeUpdate와 비교해서 코드 수행
        today = time.strptime(datetime.today().strftime("%Y/%m/%d"), "%Y/%m/%d")
        metaDay = time.strftime(self.metaData['CodeUpdate'][0], "%Y/%m/%d")
        
        if today < metaDay:
            return

        codes = pd.DataFrame(columns=['code', 'name'])
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver.exe'), chrome_options=self.chrome_options)
        driver.get("https://www.aladin.co.kr/home/wbookmain.aspx")
        html = self.driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        
        browse_sub_list = soup.select('li.browse_sub > a')

        #extract href and text
        for li in browse_sub_list:
            codes = codes.append({'code':li.attrs['href'].split('=')[1], 'name': li.text}, ignore_index=True)
        
        #save to csv
        codes.to_csv('codes.csv', encoding='utf-8', index=False)

        #update metadata 
        self.metaDataUpdate('CodeUpdate', datetime.today().strftime("%Y/%m/%d"))

    def getBookURL(self): 

        if os.path.exists('urls.csv'): # urls.csv라는 파일이 있으면 그 파일을 읽어온다
            urls = pd.read_csv('urls.csv')
        else:
            urls = pd.DataFrame(columns=['code', 'url', 'date'])
        # url만 수집
        # 2000년도 이후에 나온 책만 수집하자. 2000년도 아래 년도 책이 등장하면 수집을 멈추고 다음 파트로 넘어간다. m
        # 수집한 책 정보를 어떻게 남길까? 크롤링 업데이트가 될 때 중복을 피할 방법을 생각해야 해.
        
        # 현재 달보다 한달 적은 달보다 예전이면 크롤링을 멈춘다.
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver.exe'), chrome_options=self.chrome_options)

        df = pd.read_csv('codes.csv')
        codes=df['code']
        
        # 책 발행 연도를 제한하기 위한 코드. 현재부터 제한연도까지 차이만큼 월수를 구함
        now_year = datetime.now().year 
        now_month = datetime.now().month
        diff = (now_month-1) + (now_year-2010) * 12

        for code in codes:
            page = 0
            loop=True
            while loop : # 원소가 없으면 종료
                url = f'https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=200&ViewType=Detail&PublishMonth={diff}&SortOrder=5&page={page}&Stockstatus=1&CID={code}&SearchOption=&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax='
                driver.get(url)
                book_list = driver.find_elements(by=By.XPATH, value="//div[@class='ss_book_box']/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/a")
                #date 조건 추가해야함. 
                # date_list = driver.find_elements(by=By.XPATH, value='//div[@class="ss_book_box"]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/div[1]/ul/li[2]')
                if len(book_list) >0 :
                    idx = 0
                    for url, date in zip(book_list, date_list): # url과 date 정보를 dataframe에 추가한다.
                        # date = re.sub('년 ','-', date.text.split(' | ')[-1].rstrip('월'))
                        # date = re.sub('[^0-9\-]', '', date)
                        url = url.get_attribute('href')
                        urls = urls.append({'code': code, 'url': url, 'date': ''}, ignore_index=True)
                        # urls = urls.append({'code': code, 'url': url, 'date': date}, ignore_index=True)
                        # print(element.get_attribute('href'))
                        idx += 1  
                
                    page += 1

                else:
                    loop = False
                
                #dataframe 저장
                urls.to_csv('urls.csv', encoding='utf-8', index=False)
        driver.quit()

if __name__ == "__main__":

    getbook = BookDBUpdater()
    getbook.getBookURL()