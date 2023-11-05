import argparse
import random

import pandas as pd

import torch

from dataset import ClassificationDataset

from transformers import BertTokenizer



def define_argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model_path', required=True)
    parser.add_argument('--train_data', required=True)
    parser.add_argument('--pretrained_model_name', type=str, required=True)

    parser.add_argument('--valid_ratio', type=float, default=.2)
    parser.add_argument('--batch_size_per_device', type=int, default=32)
    parser.add_argument('--n_epochs', type=int, default=5)

    parser.add_argument('--warmup_ratio', type=float, default=.2)


    config = parser.parse_args()
    return config

def get_dataset(fn, valid_ratio=.2):
    df = pd.read_csv(fn, encoding='utf8')

    texts, labels = df['text'], df['category_num']

    # get number of class 
    unique_labels = list(set(labels))

    # Generate label to index map.
    label_to_index = {}
    index_to_label = {}
    for i, label in enumerate(unique_labels):
        label_to_index[label] = i
        index_to_label[i] = label

    # Convert label text to integer value.
    labels = list(map(label_to_index.get, labels))

    # Shuffle data before split into train and validation set.
    zipedData = list(zip(texts, labels))
    random.shuffle(zipedData)

    texts = [row[0] for row in zipedData]
    labels = [row[1] for row in zipedData]
    idx = int(len(texts) * (1-valid_ratio)) # validation 셋을 구할 index 기준점
    
    train_dataset = ClassificationDataset(texts[:idx], labels[:idx])
    valid_dataset = ClassificationDataset(texts[idx:], labels[idx:])

    return train_dataset, valid_dataset, index_to_label


def main(config):
    
    # Load pretrained Tokenizer from huggingface
    tokenizer = BertTokenizer.from_pretrained(config.pretrained_model_name)
    
    # get dataset and index to label map
    train_dataset, valid_dataset, index_to_label = get_dataset(
        config.train_data,
        valid_ratio = config.valid_ratio
    )

    # Show length of datasets
    print(
        '|train| = ', len(train_dataset),
        '|valid| = ', len(valid_dataset),
    )
    # Show map of index and label
    for i in index_to_label:
        print(i)

    # Set Hyper-parameters 1
    total_batch_size = config.batch_size_per_device * torch.cuda.device_count()
    n_total_iterations = int(len(train_dataset) / total_batch_size * config.n_epochs)
    n_warmup_step = int(n_total_iterations * config.warmup_ratio)

if __name__=='__main__':
    config = define_argparser()
    main(config)