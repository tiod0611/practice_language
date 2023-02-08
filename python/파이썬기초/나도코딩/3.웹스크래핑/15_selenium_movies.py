'''
2-1
Google Play 영화에서 할인하는 영화 정보만 스크래핑 하는 프로그램
'''

import requests
from bs4 import BeautifulSoup

from user_agent import generate_user_agent

userAgent = generate_user_agent(os='win', device_type="desktop")
headers = {
    "User-Agent":userAgent,
    "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    }


url = "https://play.google.com/store/movies"
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# 모든 영화에 대한 정보를 가져온다.
# 가져온 영화 제목을 출력하기.
movies = soup.find_all('div', attrs={"class":"zuJxTd"})
saled_movies = movies[1]
movies = saled_movies.find_all("div", attrs={"class":"ULeU3b neq64b"})
## Q: soup 객체 안에서 클래스를 어떻게 발견할까
## A: 상위 태그의 soup객체를 만든 후에 하위 태그를 찾음

movies_name = []
for movie in movies:
    name = movie.find("div", attrs={"class":"Epkrse"}).text
    movies_name.append(name)
print(movies_name)

# print(len(movies))
# print(movies[0].text)
