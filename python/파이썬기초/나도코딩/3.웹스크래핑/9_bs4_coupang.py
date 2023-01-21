# 페이지 순회하며 저장이 잘 안됨. 수정해야함

import requests
import re
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent

import pandas as pd
pd.set_option('display.max_rows', None)

import warnings 
warnings.filterwarnings(action='ignore')

# 오류 위치를 출력하는 모듈
import traceback

# 브라우저 헤더 설정
# userAgent = generate_user_agent(os='win', device_type="desktop")
# print(userAgent)
userAgent="Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0)"
headers = {"User-Agent":userAgent,
           "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}


# 페이지를 순회하며 크롤링
pageNum = 1
while pageNum < 10:
    try:
        # url에 {}로 page번호 증가
        url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={pageNum}&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
        pageNum += 1

        # 웹페이지 요청
        res = requests.get(url, headers=headers)
        res.raise_for_status() # 응답 없을 시 종료


        soup = bs(res.text, "lxml")
        items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

        # DF 만들기
        itemInfo = pd.DataFrame(columns=["name", "price", "rate", "rating_count"]) 
        
        # soup 요소를 순회하며 필요한 정보 저장
        for item in items:
            name = item.find("img", attrs={"class":"search-product-wrap-img"})['alt']
            price = item.find("strong", attrs={"class":"price-value"})
            if price: # price 값이 있으면
                price = price.get_text()
                price = int(price.replace(",","")) # str에서 ,를 모두 제거하고 int로 변경
            else:
                price = None
            
            rate = item.find("span", attrs={"class":"star"})  
            if rate: # rate 값이 있으면
                rate = float(rate.get_text())
                rating_count = item.find("span", attrs={"class":"rating-total-count"}).get_text()
                rating_count = rating_count.lstrip("(").rstrip(")")
                rating_count = int(rating_count)
            else:
                rate = None
                rating_count = None

            # DF에 새로운 행으로 데이터 저장
            itemInfo.loc[len(itemInfo)] = [name, price, rate, rating_count]
            
    except Exception as e:
        print(traceback.format_exc())
        continue

# 저장
itemInfo.to_csv("노트북 자료.tsv", mode='w', encoding='utf-8', sep="\t", index=False)


