# print("Hello World!")

# # 퀴즈 1. 변수를 이용하여 다음 문장을 출력

# station = ["사당", "신도림", "인천공항"]

# print("{} 행 열차가 들어오고 있습니다.".format(station[0]))
# print(f"{station[1]} 행 열차가 들어오고 있습니다.")
# ============================연산자==============================

# # 연산자 - 퀴즈
# # 퀴즈 2. 월 중 특정 날짜를 뽑는 코드를 짜보자. 

# from random import randint

# randDay = randint(4, 29)
# print("오프라인 스터디 모임 날짜는 매월 {} 일로 선정되었습니다.".format(randDay))
# ============================문자열==============================

# # 문자열 - 퀴즈
# # 퀴즈 3. 사이트별로 비밀번호를 만들어주는 프로그램을 작성해보자.

# # 규칙 1. http:// 부분은 제거한다
# # 규칙 2. 처음 만나는 .이후 부분은 제거한다.
# # 규칙 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내에 'e' 갯수 + !로 구성한다

# siteUrl = 'http://naver.com'
# rule1 = siteUrl.split('//')[-1] # siteUrl.replace("http://", "")
# rule2 = rule1.split('.')[0] # stieUrl[:siteUrl.index(".")]
# result = rule2[:3]+str(len(rule2))+str(rule2.count('e'))+"!"
# print(result)

# ============================자료구조==============================

# 자료구조 - 퀴즈
# 퀴즈 4. 댓글 이벤트를 개최. 추첨으로 1명은 치킨, 3명은 커피를 받게 됨

# 규칙 1. 댓글작성자는 20명이고 아이디는 1~20이라고 가정
# 규칙 2. 댓글 내용과 상관 없이 무작위로 추첨하고, 중복은 불가함
# 규칙 3. random 모듈의 shuffle과 sample을 활용

# (출력 예시)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# from random import shuffle, sample, randint

# # 이벤트 참가자 리스트 행성
# participantList = [x for x in range(1, 21)] 

# # 1등 선출
# chicken = sample(participantList, 1)

# # 1등을 후보에서 제거함
# participantList.remove(chicken[0])
# print(participantList)

# # sample을 통해 중복을 허용하지 않는 표본추출
# coffeeis = sample(participantList, 3)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {}".format(chicken[0]))
# print("커피 당첨자 : {}".format(coffeeis))
# print("-- 축하합니다 --")

# ============================제어문==============================

# 택시기사가 원하는 소요시간의 승객과 매칭하는 코드
# 조건 1. 승객별 소요 시간은 5~50분 사이의 난수
# 조건 2. 승객의 시간 5~15분 사이면 매칭한다.

# from random import randint

# check = 0 # 탑승한 승객 수를 체크하는 변수

# for i in range(1, 51):
#     DrivTime = randint(5, 51)
    
#     if DrivTime <= 15: # 원하는 손님이라면
#         check += 1
#         print("[O] {}번째 손님 (소요시간 : {}분)".format(i, DrivTime))
#     else: # 원하는 손님이 아니라면
#         print("[ ] {}번째 손님 (소요시간 : {}분)".format(i, DrivTime))
# print("총 탑승 승객 : {} 분".format(check))

# ============================함수==============================

# 퀴즈 6 표준 체중을 구하는 프로그램을 작성

# 공식
# 남자: 키^2 * 22
# 여자: 키^2 * 21

# 조건 1: 표준 체중은 함수 내에서 계산
#     ㄴ 함수명: std_weight
#     ㄴ 전달값: 키(height), 성별(gender)

# 조건 2: 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height, gender):
    if gender == "man":
        weight = height**2 * 22
        print("키 {}cm 남자의 표준 체중은 {:.2f}kg 입니다.".format(height, weight))
    elif gender =="woman":
        weight = height**2 * 21
        print("키 {}cm 여자의 표준 체중은 {:.2f}kg 입니다.".format(height, weight))

std_weight(1.78, "man") #입력 단위는 m으로 할 것