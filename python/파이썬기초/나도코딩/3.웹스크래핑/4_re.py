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
        print("group", m.group()) # 일치하는 문자열 출력
        print("string", m.string) # 입력받은 문자열
        print("start", m.start()) # 일치하는 문자열의 index
        print("end", m.end()) # 마지막 index
        print("span", m.span()) # 문자열의 시작과 끝의 index

    else:
        print("매칭되지 않음")

m = p.search("good care") # 주어진 문자열 중에 일치하는 게 있는 지 확인
print_match(m)

# find_all

lst = p.findall("good care cafe") # 일치하는 모든 것을 리스트 형태로 반환
print(lst) 