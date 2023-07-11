'''
comment

길이가 같은 두 배열에서 어떤 원소끼리 꺼내어 곱한 결과를 더했을 때 가장 최솟값이 되는지 물어보는 문제.
이 문제의 핵심은 어떤 두 값의 곱이 가장 작게 나오게 하는 지를 아는 것이다.

곱의 결과가 가장 작게 하려면 한 배열에서 가장 큰 값과 다른 배열에서 가장 작은 값을 곱하면 된다. 
이를 토대로 주어진 두 배열을 정렬하되 한 배열은 큰수부터 정렬이 되도록 만든다.
그리고 각 원소를 순서대로 꺼내서 곱하면 합이 가장 작게 나올 수 있는 배열이 만들어 진다.

'''

def solution(A,B):
    sorted_reverse_A = sorted(A, reverse=True)
    sorted_B = sorted(B)

    element_wised = [a * b for a, b in zip(sorted_reverse_A, sorted_B)]

    answer = sum(element_wised)


    return answer

if __name__=="__main__":
    A = [1, 2]
    B = [3, 4]

    result = solution(A, B)
    print(result)