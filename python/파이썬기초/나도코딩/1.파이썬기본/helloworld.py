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

# # 규칙 1. http:\\\\ 부분은 제거한다
# # 규칙 2. 처음 만나는 .이후 부분은 제거한다.
# # 규칙 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내에 'e' 갯수 + !로 구성한다

# siteUrl = 'http:\\\\naver.com'
# rule1 = siteUrl.split('\\\\')[-1] # siteUrl.replace("http:\\\\", "")
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

# def std_weight(height, gender):
#     if gender == "man":
#         weight = height**2 * 22
#         print("키 {}cm 남자의 표준 체중은 {:.2f}kg 입니다.".format(height, weight))
#     elif gender =="woman":
#         weight = height**2 * 21
#         print("키 {}cm 여자의 표준 체중은 {:.2f}kg 입니다.".format(height, weight))

# std_weight(1.78, "man") #입력 단위는 m으로 할 것

# ============================입출력==============================

# 같은 형식의 파일을 50개 반복해서 만드는 코드를 작성하자
#  조건 0. 왼쪽 오른쪽 정렬과 0으로 빈공간 체우기도 사용할 것
# 조건 1. 파일명은 '1주차.txt', '2주차.txt'.. 처럼 써야한다

# import os

# path = 'C:/Users/kyeul/Desktop/code/practice_language/python/파이썬기초/나도코딩/1.파이썬기본'
# for i in range(1, 51):
#     file_name = "{}주차.txt".format(str(i).zfill(2))
#     file_path = os.path.join(path, file_name).replace('\\', '/')
    
#     with open(file_path, 'w', encoding='utf8') as file:
#         file.write('- {} 주차 주간보고 -'.format(i)+'\n')
#         file.write('부서'.ljust(10) +':'+'\n')
#         file.write('이름'.ljust(10) +':'+'\n')
#         file.write('업무 요약'.ljust(7) +':'+'\n')


# ============================클래스!==============================
# 클래스 예제

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         # self.damage = damage
#         # print("{} 유닛이 생성 되었습니다.".format(self.name))
#         # print("체력 {}, 공격력 {1}".format(self.hp, self.damage))
#         print("{} 유닛이 생성되었습니다.".format(self.name))
    
#     def move(self, location):
#         print('[지상 유닛 이동]')
#         print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되었습니다.".format(self.name))


# # Unit 클래스 상속
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage, ):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{} : {} 방향으로 공격합니다. [공격력 {}]".format(self.name, location, self.damage))
    
# class Marine(AttackUnit):
#     def __init__(self):
#         super().__init__("마린", 40, 1, 5)

#     # 스팀팩
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{} : 체력이 부족하여 스팀팩을 사용하지 못했습니다.".format(self.name))

# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         super().__init__("탱크", 200, 1, 20)
#         self.seize_mode = False
    
#     # 시즈모드
#     def SetSeizeMode(self):
#         if Tank.seize_developed == False:
#             print("탱크의 시즈모드 개발이 완료되었습니다.")
#             return 
        
#         # 시즈모드가 개발된 경우 -> 시즈모드
#         if self.seize_mode == False:
#             print("{} : 시즈모드로 전환합니다.".format(self.name))
#             self.seize_mode = True
#             self.speed = 0
#             self.damage = 70
        
#         else:
#             print("{} : 시즈모드를 해제합니다.".format(self.name))
#             self.seize_mode = False
#             self.speed = 1
#             self.damage = 20


# # 공중유닉 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):

#     #    Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player: gg")
#     print("[Player]님이 게임에서 퇴장하셨습니다.")

# game_start()

# m1 = Marine()
# m2 = Marine()

# t1 = Tank()
# t2 = Tank()

# # 유닛 일괄 관리
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(t1)
# attack_units.append(t2)

# for unit in attack_units:
#     unit.move("1ㅅ")

# #시즈모드 개발
# Tank.seize_developed = True

# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.SetSeizeMode()

# game_over()

# # 퀴즈 : 부동산 프로그램 작성하기

# # 출력 예시
# # 총 3대의 매물이 있습니다.
# # 강남 아파트 매매 10억 2010년
# # 마포 오피스텔 전세 5억 2007년
# # 송파 빌라 월세 500/50 2000년

# class House:
#     # 매물 정보 초기화
#     count = 0

#     def __init__(self, location, house_type, deal_type, price, completion_year):
        
#         # 매물 개수
#         House.count += 1
#         # 매물 정보
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print("{} {} {} {} {}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

#     def show_count():
#         print("총 {}대의 매물이 있습니다.".format(House.count))


# # 객체 생성
# property1 = House("강남", "아파트", '매매','10억', '2010년')
# property2 = House('마포', '오피스텔', '전세', '5억', '2007년')
# property3 = House('송파', '빌라', '월세', '500/50', '2000년')

# houses = []
# houses.append(property1)
# houses.append(property2)
# houses.append(property3)

# House.show_count()
# for house in houses:
#     house.show_detail()

# ============================예외처리==============================

# 의도적으로 에러 발생시키기

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try: 
#     print("한 자리 숫자 전용 계산기")
#     num1 = int(input("첫번째 숫자"))
#     num2 = int(input("두번째 숫자"))

#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값: {}, {}".format(num1, num2))

#     print(num1, num2)

# except ValueError:
#     print("한자리만 넣으세요")

# except BigNumberError as e:
#     print("제발~! 한자리만 넣으세요")
#     print(e)

# # 코드의 정상/비정상과 관계없이 반드시 실행되는 부분
# finally:
#     print('여기는 반드시 실행됩니다.')

# 퀴즈 치킨 자동 주문 시스템

# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError  
#         출력 메시지: "잘못된 값을 입력하였습니다."

# 조건 2 : 치킨량은 10마리, 치킨 소진시 사용자 정의 에러[SoldOutError]를 발생 후 종료
#         출력 메시지: "w재고가 소진되어 더 이상 주문을 받지 않습니다."

# 코드

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


chicken = 10
waiting = 1 # 홀 안엔느 현재 만석. 대기번호 1부터 시작

while(True):
    try:
        print('[남은 치킨 : {}]'.format(chicken))
        
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        print(type(order))
        if str(type(order)) != "<class 'int'>" or order < 1:
            raise ValueError

        if order > chicken: #남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다")
        
        else:
            print("[대기번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            
        if chicken <= 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")

    except ValueError:
        print("잘못된 값을 입력하였습니다. ")
        continue

    except SoldOutError as e:
        print(e)
        break