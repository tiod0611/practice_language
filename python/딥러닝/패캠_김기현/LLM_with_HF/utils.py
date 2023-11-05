# 각종 유틸리티 모듈 스크립트

def read_text(fn):
    with open(fn, 'r') as f:
        lines = f.readlines() # 파일에서 데이터를 읽어 옴

        labels, texts = [], []
        for line in lines:
            if line.strip() != '': # line이 비어있지 않다면
                # 파일은 반드시 tab을 통해 두 컬럼으로 되어있어야 한다.
                # 첫 번째 컬럼은 레이블 필드고
                # 두 번째 컬럼은 text 데이터 필드다.
                try:
                    label, text = line.strip().split('\t') # 
                    labels += [label]
                    texts += [text]
                
                except Exception as e:
                    # 문제가 있는 line은 출력
                    print(e)
                    print(line)
                    continue
    
    return labels, texts