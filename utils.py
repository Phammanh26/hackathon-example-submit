from transformers import AutoTokenizer
import torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np

from transformers import AutoTokenizer
import torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np


class TextProcessing:
    def __init__(self, max_length: int, batch_size: int, shuffle=False) -> None:
        """
        :param max_length: The maximum length of the input sequence
        :param batch_size: The number of samples to be processed in a single batch
        :param shuffle: Whether to shuffle the data or not, defaults to False (optional)
        """
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-cased', do_lower_case=False,
                                                       use_fast=False)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.max_length = max_length
        self.batch_size = batch_size
        self.shuffle = shuffle

    def add_subword(self, sentence: str) -> list:
        """
        It takes a sentence and returns a list of subwords.
        :param sentence: The sentence to be tokenized
        :return: A list of subwords
        """
        tokenized_sentence = []
        for word in sentence.split():
            subwords = self.tokenizer.tokenize(word)
            tokenized_sentence.extend(subwords)
        return tokenized_sentence



