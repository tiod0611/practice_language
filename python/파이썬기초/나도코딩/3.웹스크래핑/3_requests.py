import requests

res = requests.get("http://google.com")

# 응답에 문제가 있을 경우 즉시 종료
res.raise_for_status

print("응답코드 :", res.status_code) # 200이면 응답이 정상으로 됨.

if res.status_code == requests.codes.ok:
    print("정상입니다")

else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code,"]")



print(len(res.text))
# print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as webpage:
    webpage.write(res.text)