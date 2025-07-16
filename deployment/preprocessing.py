
"""
Preprocessing Functions

"""

import re
import nltk
import pandas as pd
import numpy as np


def text_cleaning(text):
    
    # remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)

    #remove mentions
    text = re.sub(r'@\w+', '', text)

    # remove non-alphabetix characters
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # Handle RT tags
    text = re.sub(r'[Rr][Tt]', '', text)

    # lowercasing 
    text = str.lower(text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip() 

    return text

def tokenizer_lemmatizer(text):

    # Create tokens for the words
    tokens = nltk.word_tokenize(text)

    #instantiate lemmatizer
    lematizer = nltk.WordNetLemmatizer()

    # Create lemmas for the tokenized words
    lemmas = [lematizer.lemmatize(token) for token in tokens]

    return " ".join(lemmas)

def feature_engineer(text):

    # Count of characters in a text
    chars_count = len(text)

    # Count of words in a text
    words_count= len(nltk.word_tokenize(text))

    # Count of sentences within a text
    sentence_count = len(nltk.sent_tokenize(text))

    return [chars_count, words_count, sentence_count]


def apply_text_cleaning(x):
    if isinstance(x, list):
        x = pd.Series(x)
    return x.apply(text_cleaning)

def apply_tokenizer_lemmatizer(x):
    if isinstance(x, list):
        x = pd.Series(x)
    return x.apply(tokenizer_lemmatizer)

def apply_feature_engineer(x):
    if isinstance(x, list):
        x = pd.Series(x)
    return np.vstack(x.apply(feature_engineer))
