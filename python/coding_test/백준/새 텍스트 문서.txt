'''
1052
https://www.acmicpc.net/problem/1052
'''


n, k = map(int, input().split())

# 초기 물병 수가 k 이상인 경우
if n >= k:
    count = 0
    while n >= k:
        count += n // k
        n = n // k + n % k
    print(count)

# 초기 물병 수가 k 미만인 경우
else:
    count = 0
    while True:
        new_bottle = (n + 1) // 2
        count += 1
        if new_bottle >= k:
            break
        n = new_bottle
    print(count)



