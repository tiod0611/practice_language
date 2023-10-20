import argparse

import torch
import torch.nn as nn
import torch.optim as optim

from model import ImageClassifier
from trainer import Trainer
from data_loader import get_loaders

def define_argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model_fn', required=True)
    parser.add_argument('--gpu_id', default=0 if torch.cuda.is_available() else -1)
    parser.add_argument('--train_ratio', type=float, defualt=0.8)
    parser.add_argument('--batch_size', type=int, default=256)
    parser.add_argument('--n_epoch', type=int, default=20)
    parser.add_argument('--verbose', type=int, default=2)

    config = parser.parse_args()

    return config

def main(config):
    device = torch.device('cpu') if config.gpu_id < 0 else torch.device('cuda:%d' %config.gpu_id)

    train_loader, valid_loader, test_loader = get_loaders(config)

    print("train_loader: ", len(train_loader))
    print("valid_loader: ", len(valid_loader))
    print("test_loader: ", len(test_loader))

    # keep going after to write model.py
    model = ImageClassifier(28*28, 10).to(device)
    optimizer = optim.Adam(model.parameters())
    crit = nn.NLLLoss()

    # keep goint after to write trainer.py