def solution(s):
    answer = len(s)
    pattern_length = 1  
    
    for i in range(1, int(len(s)/2)+1):
        case_obj = s
        pattern_list = []

        while pattern_length < len(case_obj):

            pattern_obj =  case_obj[:pattern_length]
            case_obj = case_obj[pattern_length:]

            pattern_list.append(pattern_obj)
            pattern_list.append(1)


            while pattern_obj == case_obj[:len(pattern_obj)]:
                pattern_list[-1] += 1
                case_obj = case_obj[pattern_length:]

        str_pattern_list = [str(item) for item in pattern_list if item != 1]
        s_length = ''.join(str_pattern_list) + case_obj

        if answer > len(s_length):
            answer = len(s_length)
            
        pattern_length += 1

    return answer