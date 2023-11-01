from torch.utils.data import Dataset, DataLoader



class dataset(Dataset):

    def __init__(self, dataframe, tokenizer, max_len):
        self.data = dataframe
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.data)
    

    def __getitem__(self, index):
        #