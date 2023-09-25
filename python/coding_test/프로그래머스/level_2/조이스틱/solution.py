'''
https://school.programmers.co.kr/learn/courses/30/lessons/42860
조이스틱

comment

풀이 중

고려해야 하는 점.

이름 갯수만큼 "A"가 체워져있다.


'''

def solution(name):
    answer = 0
    alphabet = [chr(ascii).upper() for ascii in range(ord('a'), ord('z')+1)]
    now = 0 # 현재 커서의 위치
    for c in name:
        
        distances = [] # list 초기화
        target = alphabet.index(c) # 알파벳의 index 번호
        distances.append(abs(now-target)) # 현재 커서 위치에서 타겟 위치의 거리
        distances.append(abs(0-target)+1) # A로 이동한 뒤 target까지의 거리
        distances.append((alphabet.index('Z')-target)+1) # Z로 이동한 뒤 타겟까지의 거리
        answer += min(distances) # 3개의 경로 중 가장 작은 값을 더함
        print(f"now: {now}({alphabet[now]}), target: {target}({c}), distances: {min(distances)}   ||  {distances}")
        now = target # 현재 커서 위치를 타겟으로 업데이트

        
    return answer


if __name__=='__main__':
    name = "ABAAABB"	
    result = solution(name)
    print(result)