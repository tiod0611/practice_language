'''
https://school.programmers.co.kr/learn/courses/30/lessons/131130#

1~100까지 숫자가 적힌 카드 더미
2~100 사이의 숫자 하나를 선택하고, 그 수 만큼의 상자를 준비

각 상자에 카드를 넣고 무작위로 섞은 후 상자에 순서대로 숫자를 입력함

+ 조건 1
첫번 째 상자 그룹이 끝나고 남은 상자가 없으면 점수는 0점으로 게임 종료
+ 조건 2
발생할 수 있는 여러 상자 그룹 중에서 많은 상자의 수와 두번째 상자의 수를 곱한 값이 게임의 점수
=== 풀이 ===
1~100은 0~99로 치환해도 문제 되지 않음

'''

import random

# 이 솔루션은 무수히 많은 그룹을 모두 계산가능한 코드. 조건에 어긋남
def solution(cards):
    answer = 1
    box_num = cards.copy()

    while True:
        start_num = random.choice(box_num) #남아 있는 card에서 하나의 index 번호를 선택
        value = start_num
        iteration = 0
        pop_num = []
        while True:
            index = value-1
            value = cards[index]
            pop_num.append(value)
            iteration += 1
            
            if value == start_num:
                break
        print("pop_num: ", pop_num)
        box_num = [num for num in box_num if num not in pop_num] # 중복 리스트 제거
        # box_num = pop_num.copy()
        print("crads: ", box_num)
        answer *= iteration
        if len(box_num)<=1: # 남은 cards가 1 보다 작으면
            break
    
    # 만약 점수가 하나도 없는 경우 1이 아니라 0을 return
    if answer == 1:
        answer = 0
    
    return answer

 # 배열이 제공된 순간 그 안에 루프는 이미 결정되어 있음. 따라서 랜덤으로 숫자를 뽑을 필요가 없다. 
def solution_1(cards):
    answer = 1
    iteration = 0
    new_cards = cards.copy()
    for _ in range(2):
        pop_box = []
        pop_box.append(new_cards[0])
        while True:
            if pop_box[0] == cards[pop_box[-1]-1]:
                break
            pop_box.append(cards[pop_box[-1]-1])
            iteration += 1
        new_cards = [num for num in cards if num not in pop_box] # cards 뭉치 업데이트
        print(new_cards)
        print(pop_box)
        if len(new_cards) <= 0: # 남은 카드가 없다면 점수는 0점
            return 0
        answer *= iteration
    return answer

def solution_2(cards):
    scores = []
    box_num = cards.copy()

    while True:
        pop_num = []
        pop_num.append(box_num[0]-1)
        while True:
            if pop_num[0] == cards[pop_num[-1]-1]:
                print("break")
                break
            pop_num.append(cards[pop_num[-1]-1])   
            # break

        box_num = [num for num in box_num if num not in pop_num] # 중복 리스트 제거
        scores.append(len(pop_num))

        print("pop: ", pop_num)
        print("box: ", box_num)
        print("score: ", scores)
        # break[3, 2, 4, 5, 1]
        if len(box_num) <= 1: # 남은 카드가 없으면 종료
            break
    #
        if len(scores) > 3: # 만약 그룹이 하나라면 점수는 0점
            return 0
    scores = sorted(scores, reverse=True)
    return scores[0] * scores[-1] # 가장 높은 점수와 그 다음 점수를 곱함.

cards = [i+1 for i in range(random.randint(2, 10))]
random.shuffle(cards)
cards = [3, 2, 4, 5, 1]
print(cards)
result = solution_2(cards)

print(result)