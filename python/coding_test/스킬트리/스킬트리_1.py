def solution(skill, skill_trees):

    skills = skill
    skill_trees

    valid_num = len(skill_trees) #조합 가능한 숫자

    for item in skill_trees:
        sequence = [] # 스킬이 위치한 idx값을 담을 리스트

        for skill in skills:
            idx = item.find(skill)
            sequence.append(idx)

        for i in range(1, len(sequence)):
            # 1) 음수 뒤에 자연수가 나오면 탈락
            # 2) 자연수가 순차적으로 증가하지 않으면 탈락

            e_n = sequence[i]
            e_n_1 = sequence[i-1]

            # check_1 음수와 자연수 순서 판별
            if e_n_1 == -1 and e_n > 0:
                valid_num -= 1
                break # 더 볼 필요 없으니 검사 종료
            
        
        # 음수 검사를 통과했으니 -1 모두 제거

        sequence = [x for x in sequence if x != -1]

        for i in range(1, len(sequence)):

            e_n = sequence[i]
            e_n_1 = sequence[i-1]


            result = e_n - e_n_1 # 뒤 원소에서 바로 앞 원소의 차를 구함
            if result < 0:
                valid_num -= 1
                break

    answer = valid_num
    return answer

skills = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skills, skill_trees))
    
                    