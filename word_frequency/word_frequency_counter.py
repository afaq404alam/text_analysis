from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

nltk.download('stopwords')


def word_frequency(text):
    """
    Calculates word frequency for a given text. We don't consider stop words when calculating frequency.
    :param text: The text.
    :return: A dictionary of (word, count).
    """
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    stop = set(stopwords.words('english'))
    tokens_without_stop = list(filter(lambda word: word.lower() not in stop, tokens))

    counts = Counter(tokens_without_stop)
    return counts


def word_frequency_data_for_d3(text):
    """
    Returns word frequency in format suitable for d3 to use. Returns top 250 words only so that it fits on UI.
    This limit can be taken as an input from user in future to make this function more usable.
    :param text: The text for which to calculate frequency.
    :return: A list of dictionary items with following format [{'word': '<word>', 'size': <word_count>'}, ...]
    """
    counts = word_frequency(text)
    list_for_d3 = [{'text': word, 'size': count} for word, count in counts.items() if len(word) > 1 and len(word) > 2]
    sorted_list = sorted(list_for_d3, key=lambda item: item['size'], reverse=True)
    return sorted_list[:250]
