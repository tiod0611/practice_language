def read_text(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()

        labels, texts = [], []
        for line in lines:
            if line.strip() != '': # line이 비어있지 않으면 양쪽의 공백을 제거
                # The file should have tab delimited two columns. # 파일은 반드시 탭으로 구별된 두 컬럼을 가져야함.
                # First column indicates label field, # 첫번째 column은 label field고
                # and second column indicates text field. # 두번째 column은 text field다.
                try:
                    label, text = line.strip.split('\t') # tab으로 분리하고 양쪽의 공백을 제거
                    label += [label]
                    text += [text]

                except Exception as e:
                    print(e)
                    print(line)
                    continue

    return labels, texts

def get_grad_norm(parameters, norm_type=2):
    # gradient의 norm을 계산하는 함수

    parameters = list(filter(lambda p: p.grad is not None, parameters)) # grad에서 parameters가 None이 아닌 것만 가져와서 list로 저장

    total_norm = 0

    try:
        for p in parameters:
            total_norm += (p.grad.data**norm_type).sum() # grad에 norm_type 승을 하고 모두 더함
        
        total_norm = total_norm ** (1. / norm_type) # 계산된 total_norm에 ^{1/norm_type} 승을 해줌.
    
    except Exception as e:
        print(e)

    return total_norm


def get_parameter_norm(parameters, norm_type=2):
    # 파라미터의 norm을 계산하는 함수
    total_norm = 0

    try:
        for p in parameters:
            total_norm += (p.data**norm_type).sum()
        total_norm = total_norm ** (1. / norm_type)
    except Exception as e:
        print(e)

    return total_norm