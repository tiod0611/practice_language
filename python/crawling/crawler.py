import pandas as pd

import sys
import os
import re
from datetime import datetime 
import time

from bs4 import BeautifulSoup

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException, TimeoutException

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    # python progress bar
    # reference: https://tjjourney7.tistory.com/14
    # 약간 변형하여 사용

    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r    %s |%s| (%s/%s) %s%s %s' % (prefix, bar, iteration+1, total,percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

class BookDBUpdater:

    def __init__(self):
        
        user_agent = "user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless') #selenium 작동시 웹 페이지를 작동하지 않음
        self.chrome_options.add_argument("--log-level=3") #log를 남가지 않음
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
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'), chrome_options=self.chrome_options)

        df = pd.read_csv('codes.csv')
        codes=df['code']
        names=df['name']
        
        # 책 발행 연도를 제한하기 위한 코드. 현재부터 제한연도까지 차이만큼 월수를 구함
        now_year = datetime.now().year 
        now_month = datetime.now().month
        diff = (now_month-1) + (now_year-2010) * 12

        for code, name in zip(codes, names):
            page = 1
            loop=True
            print(f"Now=> {name} : {code}")
            end_num = driver.find_element(by=By.XPATH, value='//*[@id="short"]/div[12]/a')
            end_num.get_attribute('href')
            end_num = int(re.sub('[^0-9]', '', end_num.get_attribute('href')))

            for page in range(end_num):
                try:
                    url = f'https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=200&ViewType=Detail&PublishMonth={diff}&SortOrder=5&page={page}&Stockstatus=1&CID={code}&SearchOption=&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax='
                    driver.get(url)
                    driver.implicitly_wait(3) # seconds
                    book_list = driver.find_elements(by=By.XPATH, value="//div[@class='ss_book_box']/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/a")
                   
                    # print("    page: ", page)
                    if len(book_list) >0 :
                        idx = 0
                        for url in book_list: # url과 date 정보를 dataframe에 추가한다.
                            url = url.get_attribute('href')
                            if url not in urls['url']:
                                urls = urls.append({'code': code, 'url': url, 'date': ''}, ignore_index=True)
                            idx += 1  
                    printProgress(page, end_num, 'Progress:', 'Complete', 1, 50)

                except TimeoutException:
                    print("\nOps! TimeOut!")

                except NoSuchWindowException:
                    print("\nOps! NosuchWindow! So, restart!")
                    driver.quit()
                    driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver.exe'), chrome_options=self.chrome_options)
        
        #dataframe 저장
        urls.drop_duplicates(['drop'])
        urls.to_csv('urls.csv', encoding='utf-8', index=False)

        driver.quit()

    def getBookInfo(self):
        
        driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'), chrome_options=self.chrome_options)

        urls = pd.read_csv('urls.csv', 'r')
        bookinfo = pd.DataFrame(columns= ['isbn13', 'title', 'sub-title', 'authors', 'translator', 'publisher', 'date', 'original_title', 'price', 'pages'])
        
        for url in urls:
            driver.get(url)
            #title
            title = driver.find_element(by=By.XPATH, value='//*[@id="Ere_prod_allwrap"]/div[3]/div[2]/div[1]/div/ul/li[2]/div/a[1]').text
            #sub_title
            sub_title=driver.find_elements(by=By.XPATH, value='//*[@id="Ere_prod_allwrap"]/div[3]/div[2]/div[1]/div/ul/li[2]/div/span')
            sub_title = sub_title[0].text if sub_title else None
            #isbn
            #page
            #categories
            #introduction
            
            #author, translator, publisher, date, original_title, keyword => 교보에 접근해서 수집




            

class ReviewUpdator():
    def __init__():
        pass





if __name__ == "__main__":

    getbook = BookDBUpdater()
    getbook.getBookURL()