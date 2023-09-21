import sys
import re


def read_regex(fn):
    regexs = []
    f = open(fn, 'r', encoding='utf-8')

    for line in f:
        if not line.startswith("#"): # str.startswith("[string]") -> 시작하는 문자열을 확인하고 Bool 리턴
            tokens = line.split('\t')

            if len(tokens) == 1:
                tokens += [' ']

            tokens[0] = tokens[0][:-1] if tokens[0].endswith('\n') else tokens[0] # tokens[0]이 \n으로 끝나면 \n을 제거. 
            tokens[1] = tokens[1][:-1] if tokens[1].endswith('\n') else tokens[1]

            regexs += [(tokens[0], tokens[1])]

    f.close()

    return regexs

if __name__ == "__main__":
    fn = sys.argv[1] # 입력의 1번째 index
    target_index = int(sys.argv[2]) # 입력의 2번째 index

    regexs = read_regex(fn)

    
    with open(sys.argv[3], 'r', encoding='utf-8') as f:
        new_file = open(sys.argv[4], 'w', encoding='utf-8')
        for line in f:
            try: # label tag안된 것은 제거
                if line.strip() != "":
                    columns = line.strip().split('\t')

                    for r in regexs:
                        columns[target_index] = re.sub(r'%s' % r[0], r[1], columns[target_index].strip())
                    
                    new_file.write('\t'.join(columns) + "\n")
                else:
                    new_file.write('\n')
            except IndexError:
                pass
    new_file.close()

