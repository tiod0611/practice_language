"""
comment
입력값 s는 문자열이다. 이를 리스트를 split메서드를 사용해서 변환하기만 하면 오답이 나온다.
리스트 내 원소가 여전히 문자열이기 때문에 적절한 대소비교가 불가능하기 때문이다.
따라서 s를 리스트로 바꿔주면서 각 원소를 정수형으로 변환해야 올바른 정답을 받을 수 있다. 

"""

def solution(s):
    n_list = [int(n) for n in s.split(" ")]
    min_n = min(n_list)
    max_n = max(n_list)
    
    answer =  str(min_n)+ ' ' + str(max_n)
    return answer


if __name__=="__main__":
    s = "-4 -2 -1 0"
    result = solution(s)

    print(result)