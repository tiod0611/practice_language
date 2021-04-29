def solution(participant, completion):
    
    runners = {}
    
    for r in participant:
        if r not in runners:
            runners[r] = 1
        else:
            runners[r] += 1
    
    for c in completion:
        runners[c] -= 1
    
    for key, value in runners.items():
        if value == 1:
            return key
    