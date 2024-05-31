
'''
https://www.acmicpc.net/status?user_id=gyul611&problem_id=9012&from_mine=1
'''
def stack_vps(ps):
    stack = []

    for p in ps:
        if p == '(':
            stack.append('(')
        elif p != '(':
            if not stack:
                return 'NO'
            stack.pop()
    
    if not stack:
        return 'YES'
    else:
        return 'NO'
        
if __name__=="__main__":

    n = int(input())

    for i in range(n):
        print(stack_vps(input()))





