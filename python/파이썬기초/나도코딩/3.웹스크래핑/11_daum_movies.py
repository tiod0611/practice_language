import requests
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent

userAgent = generate_user_agent(os='win', device_type="desktop")
headers = {"User-Agent":userAgent,
            "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}


for year in range(2015, 2023):

    url = f'https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    res = requests.get(url, headers = headers)
    res.raise_for_status()

    soup = bs(res.text, "lxml")

    imgs = soup.find_all('img', attrs={"class":"thumb_img"})

    for index, img in enumerate(imgs):
        img_url = img['src']
        if img_url.startswith("//"):
            img_url = "https:" + img_url

        print(img_url)

        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, index+1), 'wb') as f:
            f.write(img_res.content)

        if index >= 9: # 상위 5개 파일만 가져옴
            break


