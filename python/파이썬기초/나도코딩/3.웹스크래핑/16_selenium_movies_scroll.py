'''
2-2
Google Play 영화에서 할인하는 영화 정보만 스크래핑 하는 프로그램
=> youtube 페이지로 변경
목표
스크롤을 아래로 내려서 정보를 갱신하자.

======

2-3
youtube에서 영상 정보를 가져와서 pandas DataFrame에 저장하기
가져올 정보

columns=[채널명, 영상 이름, 조회수, url] 

'''
from bs4 import BeautifulSoup as bs

from selenium import webdriver
import chromedriver_autoinstaller
from user_agent import generate_user_agent

import time
import re
import pandas as pd

# generate user_agent
# userAgent = generate_user_agent(os='win', device_type="desktop")
# headers = {
#     "User-Agent":userAgent,
#     "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
#     }

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.

# chrome driver autoinstaller
driver_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(driver_path, options=options)



# url = "https://play.google.com/store/movies"
# youtube로 url 변경
url = 'https://www.youtube.com/'
driver.get(url)
driver.implicitly_wait(5)


# 지정한 위치로 스크롤 내리기
# 모니터의 해상도 높이인 1080 위치로 스크롤 내리기. 즉 가장 밑으로 내리기
# driver.execute_script("window.scrollTo(0, 1080)")
# driver.implicitly_wait(2)

# time.sleep(5)


# 화면 가장 아래로 스크롤 내리기
# document.body.scrollHeight => 브라우저 화면 높이만큼 이동함
print("화면 내리기 시작")
scroll_height = 1080
document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
while True: # 페이지 로드가 끝날 때까지 무한 로딩
    # 스크롤을 가장 아래로 내림
    driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
    # 로딩 대기
    time.sleep(1.5)

    current_height = driver.execute_script("return document.documentElement.scrollHeight")
    
    print(document_height_before, current_height)
    # 현재 높이가 갱신 전 높이와 같다면. 즉, 갱신이 되지 않았다면 종료
    if current_height == document_height_before:
        break

    document_height_before = current_height
    
    # 테스트를 위해 일단 1바퀴만 진행
    break

print("화면 내리기 종료")


'''
2-3 시작
'''

soup = bs(driver.page_source, 'lxml')

video_info = soup.find_all('div', attrs={'class':'style-scope ytd-rich-grid-media',
                                        'id':'meta'})
channels = []
video_names = []
views = []
urls = []

for info in video_info:
    try:
        ch = info.find('a', attrs={'class':'yt-simple-endpoint style-scope yt-formatted-string'}).text
        vn = info.find('h3', attrs={'class':'style-scope ytd-rich-grid-media'}).text
        view = info.find('span', attrs={'class':'inline-metadata-item style-scope ytd-video-meta-block'}).text
        view = view[4:-1] # '조회수', '회' 단어 제거
        url = info.find('a', attrs={'class':'yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media'})
        url = url['href']

        channels.append(ch)
        video_names.append(vn)
        views.append(view)
        urls.append(url)
    except Exception as e:
        print(e)
        continue

# 데이터 프레임으로 저장하기
df = pd.DataFrame(columns=['channel_name', 'video_name', 'views', 'urls'])
for idx, (ch, vn, view, url) in enumerate(zip(channels, video_names, views, urls)):
    df.loc[idx] = [ch, vn, view, url]

print(df)
