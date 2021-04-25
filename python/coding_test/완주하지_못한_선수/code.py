def solution_1(participant, completion):
    
    for runner in completion:
        participant.remove(runner)
        
    return participant[0]


print(solution_1(["leo", "kiki", "eden"], ["eden", "kiki"]))