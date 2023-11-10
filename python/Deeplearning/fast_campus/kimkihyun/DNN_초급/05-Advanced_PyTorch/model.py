import torch
import torch.nn as nn

class ImageClassfier(nn.Module):

    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

        super().__init__()

        self.layers = nn.Sequential(
            nn.Linear(self.input_size, 600),
            nn.LeakyReLU(),
            nn.BatchNorm1d(600),
            nn.Linear(600, 500),
            nn.LeakyReLU(),
            nn.BatchNorm1d(500),
            nn.Linear(500, 400),
            nn.LeakyReLU(),
            nn.BatchNorm1d(400),
            nn.Linear(400, 300),
            nn.LeakyReLU(),
            nn.BatchNorm1d(300),
            nn.Linear(300, 200),
            nn.LeakyReLU(),
            nn.BatchNorm1d(200),
            nn.Linear(200, 100),
            nn.LeakyReLU(),
            nn.BatchNorm1d(100),
            nn.Linear(100, 50),
            nn.LeakyReLU(),
            nn.BatchNorm1d(50),
            nn.Linear(50, self.output_size),
            nn.Softmax(dim=-1) # 원 코드는 LogSoftmax사용
        )

    def forward(self, x): # 이건 맞았음. 입력으로 x를 받고 출력으로 y를 뱉는다.
        y = self.layers(x)

        return y