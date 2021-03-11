"""
link: 

선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

제한 조건
스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
스킬 순서와 스킬트리는 문자열로 표기합니다.
예를 들어, C → B → D 라면 "CBD"로 표기합니다
선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
skill_trees는 길이 1 이상 20 이하인 배열입니다.
skill_trees의 원소는 스킬을 나타내는 문자열입니다.
skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.
입출력 예
skill	skill_trees	return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
입출력 예 설명
"BACDE": B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트립니다.
"CBADF": 가능한 스킬트리입니다.
"AECB": 가능한 스킬트리입니다.
"BDA": B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트리입니다.
"""
"""
case1) 스킬트리에 맞게 온 경우
case2) 스킬트리의 뒷 부분이 없는 경우(앞 나머지는 순서 ok)
case3) 스킬트리의 앞부분에 선행 스킬이 없는 경우
"""

"""
풀이 전략 1) 
1. 스킬트리이므로, 한번 익힌 스킬을 나중에 다시 배울 수 없다. 즉, 등장한 character는 다시 등장하지 않는다.
    regular expression을 사용하여 문자열의 index자리를 확인하고 skill 순서에 맞게 index가 증가하지 않는 개수만큼 list의 길이에서 빼자.
    1-1. skill중 skill_trees에 없는 것은 처음부터 제거
"""

def check_natural(sequence):
    for i in range(1, len(sequence)):
        # 원소가 순차적으로 증가하는지 판별
        # len = n
        # a_k = e_n - e_(n-1)

        e_n = sequence[i] 
        e_n_1 = sequence[i-1] 

        if e_n == -1 and e_n_1 > 0: #1항이 음수라면 패스 
            continue

        
        result = e_n - e_n_1

        if result < 0:
            return False
    return True    



def solution(skill, skill_trees):
    
    skills = skill
    valid_num = len(skill_trees)
    
    # # 버전 1
    # for item in skill_trees:
    #     pre_idx = 0
        
    #     for skill in skills:
    #         idx = item.find(skill)
            
    #         if idx - pre_idx < 0:
    #             able_num -= 1
    #             break
    #         pre_idx = idx
    
    for item in skill_trees:
        sequence =[]

        for skill in skills:
            idx = item.find(skill)
            sequence.append(idx)




        if check(sequence) == False:
            able_num -= 1


    answer = able_num
    return answer

skills = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skills, skill_trees))