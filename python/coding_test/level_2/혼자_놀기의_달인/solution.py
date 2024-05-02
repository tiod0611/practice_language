'''
https://school.programmers.co.kr/learn/courses/30/lessons/131130#
'''

import random

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


cards = [i+1 for i in range(random.randint(2, 10))]
random.shuffle(cards)
print(cards)
result = solution(cards)

print(result)