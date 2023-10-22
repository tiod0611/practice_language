from copy import deepcopy

import numpy as np

import torch
import torch.nn.functional as F
import torch.optim as optim
import torch.nn.utils as torch_utils

from ignite.engine import Engine, Events
from ignite.metrics import RunningAverage
from ignite.contrib.handlers.tqdm_logger import ProgressBar

from utils import get_grad_norm, get_parameter_norm

VERBOSE_SILENT = 0
VERBOSE_EPOCH_WISE = 1
VERBOSE_BATCH_WISE = 2

class MyEngine(Engine):

    def __init__(self, func, model, crit, optimizer, config):
        # Ignite Engine 아래 라인에는 obeject가 없음
        # 따라서 진행 중에 class 변수를 assign하려면 object에 접근해야 함.

        self.model = model
        self.crit = crit
        self.optimzer = optimizer
        self.config = config

        super().__init__(func) # Ignite Engine은 실행을 위해 function만 필요하다.

        self.best_loss = np.inf
        self.best_model = None

        self.device = next(model.parameters()).device

    @staticmethod
    def train(engine, mini_batch):
        # 모든 모델 파라미터의 gradient를 reset해야 한다.
        # gradient descent의 step을 하기 전에

        engine.model.train() # 
        engine.optimzer.zero_grad()

        x, y = mini_batch
        x, y = x.to(engine.device), y.to(engine.device)

        # feed-forward 수행
        y_hat = engine.model(x)

        loss = engine.crit(y_hat, y)
        loss.backward()

        # y가 LongTensor라면 accuracy를 계산한다
        # 즉 y가 one-hot representation임을 뜻한다.

        if isinstance(y, torch.LongTensor) or isinstance(y, torch.cuda.LongTensor):
            accuracy = (torch.argmax(y_hat, dim=-1) == y).sum() / float(y.size(0))
        else:
            accuracy = 0

        p_norm = float(get_parameter_norm(engine.model.parameters()))
        g_norm = float(get_grad_norm(engine.model.parameters()))

        # Take a step of gradient descent.
        engine.optimizer.step()

        return {
            'loss': float(loss),
            'accuracy': float(accuracy),
            '|param|': p_norm,
            '|g_param|': g_norm,
        }
    
    @staticmethod
    def validate(engine, mini_batch):
        engine.model.eval() # 미분 off

        with torch.no_grad():
            x, y = mini_batch
            x, y = x.to(engine.device), y.to(engine.device)

            y_hat = engine.model(x)
            
            loss = engine.crit(y_hat, y)

            if isinstance(y, torch.LongTensor) or isinstance(y, torch.cuda.LongTensor):
                accuracy = (torch.argmax(y_hat, dim=-1) == y).sum() / float(y.size(0))
            else:
                accuracy = 0

        
        return {
            'loss' : float(loss),
            'accuracy' : float(accuracy),
        }
    
    @staticmethod
    def attach(train_engine, validation_engine, verbose=VERBOSE_BATCH_WISE):
        # 