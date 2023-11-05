# v.0.1 쿠팡에서 특정 키워드로 검색된 결과물에 대해 이름, 가격, 평점을 수집하는 크롤러
# v.0.2 품절된 제품은 수집 제외



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


# rquests와 BeautifulSoup 실행
def getReqeustsAndParsing(url, pageNum, headers):
    
    res = requests.get(url, headers=headers)
    res.raise_for_status() # 응답 없을 시 종료
    print("page: {} 진행 중..".format(pageNum))

    return bs(res.text, "lxml")


def getLastPageNum(soup):
    
    lastPage = soup.find("a", attrs={"class":"btn-last disabled"}).get_text()
    return int(lastPage)

# 특정 키워드가 포함된 행 제거
def removeKeywordRow(keyword, itemInfo):
    pass





# 페이지를 순회하며 크롤링
def getItemInfo(soup, itemInfo, sort = True):
    try:
        items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
        for item in items:

                # 품절된 제품이 있으면 기록
                soldOut = item.find("div", attrs={"class":"out-of-stock"})
                if soldOut:
                    is_soldout = True
                else:
                    is_soldout = False         

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
                itemInfo.loc[len(itemInfo)] = [name, price, rate, rating_count, is_soldout]
        
        
        if sort:
            itemInfo.sort_values(by=['rating_count', 'rate'], ascending=False)

        return itemInfo

    except Exception as e:
        # print(traceback.format_exc())
        print(e)
        pass


# 저장
def saveToTsv(name, itemInfo):
    itemInfo.to_csv(f"{name} 자료.tsv", mode='w', encoding='utf-8', sep="\t", index=False)



if __name__ == "__main__":

    # DF 만들기
    itemInfo = pd.DataFrame(columns=["name", "price", "rate", "rating_count", "is_soldOut"])
   
    # 초기값 설정
    pageNum = 1
    # keyword = input()
    name = "노트북"

    # 브라우저 헤더 설정
    # userAgent = generate_user_agent(os='win', device_type="desktop")
    # print(userAgent)
    userAgent="Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0)"
    headers = {"User-Agent":userAgent,
            "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    # 페이지 마지막 번호 알아내기
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=72&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={pageNum}&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
    soup = getReqeustsAndParsing(url, pageNum, headers)
    
    lastPage = getLastPageNum(soup)
    itemInfo = getItemInfo(soup, itemInfo)
    
    # 페이지 수 만큼 반복을 실행
    for pageNum in range(2, lastPage+1):
        soup = getReqeustsAndParsing(pageNum, headers)
        itemInfo = getItemInfo(soup, itemInfo)

    
    saveToTsv(name, itemInfo)
    

    