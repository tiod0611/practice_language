import torch
from torch.utils.data import Dataset

class TextclassificationCollator():
    # data 길이를 동일하게 맞춰주는 작업

    def __init__(self, tokenizer, max_lenght, with_text=True):
        self.tokenizer = tokenizer
        self.max_lenght = max_lenght
        self.with_text = with_text

    def __call__(self, samples): # collate function을 호출하면 실행됨.
        '''
        samples: list in dictionary
        '''
        texts = [s['text'] for s in samples] # 
        labels = [s['label'] for s in samples]

        encoding = self.tokenizer(
            texts,
            padding=True,
            truncation=True, #
            return_tensor='pt', #pytorch type
            max_length=self.max_length
        )

        return_value = {
            'input_ids' : encoding['input_ids'],
            'attention_mask' : encoding['attention_mask'], #
            'labels' : torch.tensor(labels, dtype=torch.long)
        }
        # text 원본이 필요한 경우
        if self.with_text:
            return_value['text'] = texts

        return return_value
    
class TextCalssificationDataset(Dataset):

    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, item):
        text = str(self.texts[item])
        label = self.labels[item]

        return {
            'text':text,
            'label':label
        }

