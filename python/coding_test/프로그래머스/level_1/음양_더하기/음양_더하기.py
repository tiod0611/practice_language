def solution(absolutes, signs):
    answer = list(map(lambda x, s: x if s == True else x * -1, absolutes, signs))
    return sum(answer)