'''
comment
탐욕 알고리즘

탐욕 알고리즘이란, 눈앞에 놓인 조건에서 가장 이득이 되는 조건을 찾는 알고리즘이다.
예를 들면, 1490원을 가장 적은 갯수의 잔돈으로 만들 때 사용할 수 있다.

이 문제도 마찬가지다. 
가장 무거운 사람을 기준으로, 이 사람이 가장 가벼운 사람과 합쳤을 때 무게 제한을 넘어간다면 당연히 혼자 탑승해야 한다.
두 사람의 합이 무게 제한을 넘지 않는다면, 가장 무거운 사람과 가장 가벼운 사람이 최선의 짝이 된다. 
이 과정을 반복하면 모두 안전하게 탈출할 수 있다. 

'''


def solution(people, limit):
    boat = 0
    people = sorted(people, reverse=True)

    start, end = 0, len(people) - 1 # 배열이 처음과 끝

    while start <= end:
        # 가장 무거운 사람과 가벼운 사람의 합이 무게제한보다 가볍다면,
        if people[start] + people[end] <= limit:
            end -= 1 # 가벼운 사람도 탑승하여 떠나기 때문에 배열에서 제거된다.
        # 그렇지 않다면 무거운 사람만 떠났기 때문에 앞쪽 index값만 증가시킨다.
        start += 1
        boat += 1 # 보트 한대가 떠난다. 

    return boat


if __name__=='__main__':
    people = [70, 50, 80, 50]
    limit = 100
    result = solution(people, limit)
    print(result)