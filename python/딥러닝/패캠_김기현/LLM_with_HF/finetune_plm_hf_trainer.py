import argparse
import random

import torch

from transformers import BertTokenizerFast


from utils import read_text
from bert_dataset import TextClassificationDataset

def define_argparser():
    p = argparse.ArgumentParser()

    p.add_argument('--model_fn', required=True)
    p.add_argument('--train_fn', required=True)

    # 아래는 pre-trained model을 입력받는데, 추천리스트가 있음
    # 1. kykim/bert-kor-base
    # 2. kykim/albert-kor-base
    # 3. beomi/kcbert-base
    # 4. beomi/kcbert-large
    p.add_argument('--pretrained_model_name', type=str, default='beomi/kcbert-base')
    
    #  아래 인자는 사용할 text classifier을 선택한다
    p.add_argument('--use_albert', action='store_true') 
    p.add_argument('--use_roberta', action='store_true')  

    # parameter setting
    p.add_argument('--valid_ratio', type=float, default=.2)
    p.add_argument('--batch_szie_per_device', type=int, default=32) # 배치사이즈
    p.add_argument('--n_epochs', type=int, default=10)

    p.add_argument('--warmup_ratio', type=float, default=.2) # 초기 학습률 도달까지 낮은 학습률로 시작하는 단계(?). 이게 왜 효과적이지? -> 초기 랜덤값에 높은 lr을 설정하면 학습이 잘 안될 수 있다. 이를 방지하기 위해 낮은 값에서 점점 도달하게 함
    p.add_argument('--max_length', type=int, default=100) # token 사이즈

    config = p.parse_args()

    return config

def get_datasets(fn, valid_ratio=.2):
    # Get list of labels and list of texts.
    labels, texts = read_text(fn)

    # Generate label to index map.
    unique_labels = list(set(labels))
    label_to_index = {}
    index_to_label = {}
    
    # mapping 
    # 어떻게 활용할지는 살펴보자.
    for i, label in enumerate(unique_labels):
        label_to_index[label] = i # {'class1':1, 'class2':2}
        index_to_label[i] = label # {1: 'class1', 2:'class2'}


    # Convert label text to integer value.
    labels = list(map(label_to_index.get, labels)) # integer로 매핑된 list를 반환함

    # Shuffle before split into train and validation set.
    shuffled = list(zip(texts, labels))
    random.shuffle(shuffled) 
    
    texts = [text[0] for text in shuffled]
    labels = [labels[1] for labels in shuffled]
    idx = int(len(texts) * (1-valid_ratio)) # lengths of training dataset

    train_dataset = TextClassificationDataset(texts[:idx], labels[:idx])
    valid_dataset = TextClassificationDataset(texts[idx:], labels[idx:])

    return train_dataset, valid_dataset, index_to_label

def main(config):
    # Get pretrained tokenizer
    tokenizer = BertTokenizerFast.from_pretrained(config.pretrained_model_name) 

    # Get datasets and index to label map.
    train_dataset, valid_dataset, index_to_label = get_datasets(
        config.train_fn,
        valid_ratio=config.valid_ratio
    )

    print(
        '|train| =', len(train_dataset),
        '|valid| =', len(valid_dataset)
    )

    # set batch, iteration, warmup_size
    total_batch_size = config.batch_size_per_device * torch.cuda.device_count()
    n_total_iterations = int(len(train_dataset)/total_batch_size * config.n_epochs)
    n_warmup_steps = int(n_total_iterations * config.warmup_ratio) # 전체 반복에서 웜업 비율만큼 웜업함
    print(
        '# total_iters =', n_total_iterations,
        '# warmup_iters =', n_warmup_steps
    )

    # Get pretrained model with specified softmax layer.
    assert not (config.use_albert and config.use_roberta), 'Only one of use_albert and use_roberta can be True.'
    



if __name__=='__main__':
    '''
    파일을 호출시 실행
    '''
    config = define_argparser() # configuration 값을 사용자로부터 받음
    main(config) # 메인 함수 실행