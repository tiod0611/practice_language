import torch
from torch.utils.data import Dataset, DataLoader

class MnistDataset(Dataset):
    # Dataset 클래스 정의

    def __init__(self, data, labels, flatten=True):
        self.data = data
        self.labels = labels
        self.flatten = flatten

        super().__init__()

    
    def __len__(self):
        return self.data.size(0)
    
    def __getitem__(self, idx):
        # return batchfy dataset
        x = self.data[idx]
        y = self.labels[idx]

        if self.flatten:
            x = x.view(-1)

        
        return x, y
    

def load_mnist(is_train=True, flatten=True):
    from torchvision import datasets, transforms

    dataset = datasets.MNIST(
        '../data', train=is_train, download=True,
        transform=transforms.Compose([
            transforms.ToTensor(),
        ]),
    )

    x = dataset.data.float() / 255.
    y = dataset.targets

    if flatten:
        x = x.view(x.size(0), -1)

    return x, y

def get_loaders(config):

    # 데이터 로더에 보낼 데이터 전처리
    x, y = load_mnist(is_train=True, flatten=False)

    # 비율에 맞춰 split
    train_cnt = int(x.size(0) * config.train_ratio)
    valid_cnt = x.size(0) - train_cnt

    # Shuffle
    indices = torch.randperm(x.size(0))
    train_x, valid_x = torch.index_select(
        x, 
        dim=0,
        index=indices
    ).split([train_cnt, valid_cnt], dim=0)
    train_y, valid_y = torch.index_selct(
        y, 
        dim=0,
        index=indices
    ).split([train_cnt, valid_cnt], dim=0)


    # 데이터 로더 정의
    train_loader = DataLoader(
        dataset=MnistDataset(train_x, train_y, flatten=True),
        batch_size=config.batch_size,
        shuffle=True,
    )
    valid_loader = DataLoader(
        dataset=MnistDataset(valid_x, valid_y, flatten=True),
        batch_size=config.batch_size,
        shuffle=True,
    )

    # 지정된 테스트셋이므로 shuffle은 없다.
    test_x, test_y = load_mnist(is_train=True, flatten=False)
    test_loader = DataLoader(
        dataset=MnistDataset(test_x, test_y, flatten=True),
        batch_size=config.batch_size,
        shuffle=False,
    )

    return train_loader, valid_loader, test_loader