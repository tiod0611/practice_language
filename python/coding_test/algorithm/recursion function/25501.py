import sys
input = sys.stdin.readline

def recursion(s, l, r, count):
    count += 1
    if l >= r:
        return 1, count
    elif s[l] != s[r]:
        return 0, count
    else:
        return recursion(s, l + 1, r - 1, count)

def is_palindrome(s):
    return recursion(s, 0, len(s) - 1, 0)

if __name__ == '__main__':
    n = int(input().rstrip())
    for _ in range(n):
        s = input().rstrip()
        result, count = is_palindrome(s)
        print(result, count)