# 정규식 기초

import re

p = re.compile("ca.e") 
# . : 하나의 문자를 의미
# ^ : 문자열의 시작
# $ : 문자열의 끝
# () : 묶어서
# [] : 있거나 없거나

m = p.match("case")
print(m.group())

# 매칭이 안된 경우
m = p.match("caffe")
# print(m.group())

if m:
    print(m.group) 
    # 에러는 match에서 나는 게 아니라 group()에서 발생함
else:
    print("안됨")


#  match용 함수
def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")