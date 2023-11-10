import argparse
import random

import pandas as pd
from sklearn.metrics import accuracy_score

import torch

from dataset import ClassificationDataset
from dataset import ClassificationCollator

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import Trainer
from transformers import TrainingArguments



def define_argparser(pretrained_model_name, epochs):
    parser = argparse.ArgumentParser()

    parser.add_argument('--train_data_path', required=True)
    parser.add_argument('--model_path', required=True)
    parser.add_argument('--pretrained_model_name', type=str, default=pretrained_model_name)

    parser.add_argument('--valid_ratio', type=float, default=.2)
    parser.add_argument('--batch_size_per_device', type=int, default=32)
    parser.add_argument('--n_epochs', type=int, default=epochs)

    parser.add_argument('--warmup_ratio', type=float, default=.2)
    parser.add_argument('--max_length', type=int, default=256)


    config = parser.parse_args()
    return config

def get_dataset(fn, valid_ratio=.2):
    df = pd.read_csv(fn, encoding='utf8')

    label_map = {
    'sport':0,
    'business': 1,
    'politics': 2,
    'tech':3,
    'entertainment': 4
    }

    df['category_num'] = df['category'].map(label_map)

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
    
    # split it.
    train_dataset = ClassificationDataset(texts[:idx], labels[:idx])
    valid_dataset = ClassificationDataset(texts[idx:], labels[idx:])

    return train_dataset, valid_dataset, index_to_label


def main(config):
    
    # Load pretrained Tokenizer from huggingface
    tokenizer = AutoTokenizer.from_pretrained(config.pretrained_model_name)
    
    # get dataset and index to label map
    train_dataset, valid_dataset, index_to_label = get_dataset(
        config.train_data_path,
        valid_ratio = config.valid_ratio
    )

    # Show length of datasets
    print(
        ' |train| = ', len(train_dataset), '\n',
        '|valid| = ', len(valid_dataset), '\n',
        '|length of class| = ', len(index_to_label)
    )

    # Set Hyper-parameters 1
    total_batch_size = config.batch_size_per_device * torch.cuda.device_count()
    n_total_iterations = int(len(train_dataset) / total_batch_size * config.n_epochs)
    n_warmup_steps = int(n_total_iterations * config.warmup_ratio)

    print(
        " #total_iters =", n_total_iterations,'\n',
        "#warmup_iters =", n_warmup_steps,
    )

    # Get pretrained model with specified softmax layer
    model = AutoModelForSequenceClassification.from_pretrained(
        config.pretrained_model_name)

    training_args = TrainingArguments(
        output_dir='./.checkpoints',
        num_train_epochs=config.n_epochs,
        per_device_train_batch_size=config.batch_size_per_device,
        per_device_eval_batch_size=config.batch_size_per_device,
        warmup_steps=n_warmup_steps,
        weight_decay=0.01,
        fp16=True, # 
        evaluation_strategy='epoch',
        save_strategy='epoch',
        logging_steps=n_total_iterations // 100,
        save_steps=n_total_iterations // config.n_epochs,
        load_best_model_at_end=True,
    )

    def compute_metrics(pred):
        labels = pred.label_ids
        preds = pred.predictions.argmax(-1)

        return {
            'accuracy' : accuracy_score(labels, preds)
        }

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=ClassificationCollator(tokenizer,
                                                 config.max_length,
                                                 with_text=False),
        train_dataset=train_dataset,
        eval_dataset=valid_dataset,
        compute_metrics=compute_metrics,
    )
    trainer.train()

    torch.save({
        'bert':trainer.model.state_dict(),
        'config': config,
        'classes': index_to_label,
        'tokenizer':tokenizer,
    }, config.model_path)


if __name__=='__main__':

    # set default value for argparser
    pretrained_model_name = "abhishek/autonlp-bbc-news-classification-37229289"
    epochs = 5

    config = define_argparser(pretrained_model_name, epochs)
    main(config)
