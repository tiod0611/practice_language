import sys
sys.stdin=open('input.txt', 'rt')

T = int(input())

def solution(T):
    for i in range(T):
        _, s, e, k = map(int, input().split())
        num_list = list(map(int, input().split()))
        print(f"#{i+1}", sorted(num_list[s-1:e])[k-1])

solution(T)