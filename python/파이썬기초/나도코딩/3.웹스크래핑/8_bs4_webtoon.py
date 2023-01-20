import requests
from bs4 import BeautifulSoup as bs
import re

url='https://comic.naver.com/webtoon/list?titleId=710751&weekday=sun'

res = requests.get(url)
res.raise_for_status()

soup = bs(res.text, "lxml")

# 회차별 제목 가져오기
class_titles = soup.find_all('td', attrs={"class":"title"})
class_rating_type = soup.find_all('div', attrs={"class":"rating_type"})
titles = []
links = []
for title in class_titles:
    titles.append(title.a.get_text())
    links.append("https://comic.naver.com"+title.a['href'])
    
scores = []
for rate in class_rating_type:
    scores.append(float(rate.strong.get_text()))


for title, link, score in zip(titles, links, scores):
    print(title,":", link, "-", score)

print("Mean score: {:.2f}".format(sum(scores)/len(scores)))