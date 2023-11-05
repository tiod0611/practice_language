from bs4 import BeautifulSoup as bs
import requests

import re

url = "https://comic.naver.com/webtoon/weekday"
headers = {"headers": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = bs(res.text, "lxml") # parser : lxml

# print(soup.a.attrs) # a 엘리먼트의 속성 정보를 반환함
# print(soup.a['href']) # a 엘리먼트의 특정 속성 값을 반환함

# print(soup.find("a", attrs={"class":"Nbtn_upload"}).text)
# print(soup.find(attrs={"class":"Nbtn_upload"}).text)

ranks = []

for i in range(1, 11):
    num = '0'+str(i) if i < 10 else str(i)
    rank = soup.find("li", attrs={"class": "rank"+num})
    ranks.append(rank.a.get_text())

for i in ranks:
    print(i.split("-")[0])

# 형제 태그를 모두 살펴보는 find_next_siblings("태그")
ranks = soup.find("li", attrs={"class": "rank01"}).find_next_siblings("li")
for i in ranks:
    print(i.a.get_text().split("-")[0])