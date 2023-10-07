import torch.nn
import torch.nn as nn

class Block(nn.Module):
    
    def __init__(self, 
                 input_size, 
                 output_size,
                 use_batch_norm=True,
                 dropout_p=.4):
        self.input_size = input_size
        self.output_size = output_size
        self.use_batch_norm = use_batch_norm
        self.dropout_p = dropout_p

        super().__init__()

        def get_regularizer(use_batch_norm, size):
            return nn.BatchNorm1d(size) if use_batch_norm else nn.Dropout(dropout_p)
        
        self.block = nn.Sequential(
            nn.Linear(input_size, output_size),
            nn.LeakyReLU(),
            get_regularizer(use_batch_norm, dropout_p)
        )
    
    def forward(self, x):
        # |x| = (batch_size, input_size)
        y = self.block(x)
        # |y| = (batch_size, output_size)

        return y
    

class ImageClassifier(nn.Module):
    def __init__(self,
                 input_size,
                 output_size,
                 hidden_sizes=[500, 400, 300, 200, 100],
                 use_batch_norm=True,
                 dropout_p=.4):
        
        super().__init__()

        # hidden_size가 입력되지 않으면 layer를 쌓을 수 없기 때문에 에러를 발생하면서 프로그램 종료
        assert len(hidden_sizes) > 0, "You need to sepecify hidden layers"

        last_hidden_size = input_size
        blocks = []

        # 입력받은 hidden_size대로 block을 쌓는다.
        for hidden_size in hidden_sizes:
            # layer는 입력과 출력의 크기를 가지고 있다. (이전 output, 현재 output)
            blocks += [Block(
                last_hidden_size, # 입력 크기(이전 레이어의 출력 크기)
                hidden_size, # 출력 크기
                use_batch_norm,
                dropout_p
            )]

            last_hidden_size = hidden_size # 이전 레이어의 출력은 현재 레이어의 입력이므로 재사용을 위해 변수에 대입

        self.layers = nn.Sequential(
            *blocks, # 생성한 block들을 차례대로 쌓는다.

            # 마지막은 출력 크기로 해주고 LogSoftmax로 확률을 계산하자.
            nn.Linear(last_hidden_size, output_size),
            nn.LogSoftmax(dim=-1)
        )


    def farward(self, x):
        y = self.layers(x)

        return y