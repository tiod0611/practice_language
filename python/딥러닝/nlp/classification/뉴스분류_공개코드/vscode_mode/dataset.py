import torch
from torch.utils.data import Dataset

class ClassificationCollator():
    pass

class ClassificationDataset(Dataset):

    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, item):
        text = self.texts.iloc[item]
        label = self.labels.iloc[item]

        return text, label