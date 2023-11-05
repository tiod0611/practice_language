import requests


headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
url = "http://nadocoding.tistory.com"

res = requests.get(url, headers=headers)
res.raise_for_status() # 응답 없으면 종료

with open("nadocoding.html", "w", encoding='utf8') as f:
    f.write(res.text)